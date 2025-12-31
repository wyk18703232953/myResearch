#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
带正则化的 Pow(2, k, mod) 性能拟合分析
使用 AIC/BIC 正则化来正确选择 O(log k) 模型
"""

import time
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import warnings
warnings.filterwarnings('ignore')

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

class RegularizedFitter:
    def __init__(self):
        self.mod = 10**9 + 7
        self.k_values = []
        self.time_values = []
        self.models = {}
        
    def measure_pow_performance(self, k_values, iterations=10000):
        """测量 pow(2, k, mod) 的性能"""
        print("开始性能测试...")
        
        for k in k_values:
            start = time.perf_counter()
            for _ in range(iterations):
                pow(2, k, self.mod)
            elapsed = time.perf_counter() - start
            self.k_values.append(k)
            self.time_values.append(elapsed)
            print(f"k={k:>20}, time={elapsed:.6f}s")
        
        return self.k_values, self.time_values
    
    # 定义各种时间复杂度模型
    @staticmethod
    def constant_model(k, a):
        """O(1) 常数模型"""
        return np.full_like(k, a, dtype=float)
    
    @staticmethod
    def linear_model(k, a, b):
        """O(k) 线性模型"""
        return a * k + b
    
    @staticmethod
    def log_model(k, a, b):
        """O(log k) 对数模型"""
        return a * np.log2(k) + b
    
    @staticmethod
    def sqrt_model(k, a, b):
        """O(sqrt(k)) 平方根模型"""
        return a * np.sqrt(k) + b
    
    @staticmethod
    def log_linear_model(k, a, b):
        """O(k log k) 对数线性模型"""
        return a * k * np.log2(k) + b
    
    @staticmethod
    def power_model(k, a, b, c):
        """O(k^b) 幂模型"""
        return a * np.power(k, b) + c
    
    def calculate_information_criteria(self, residuals, n_params, n_samples):
        """计算信息准则来惩罚复杂模型"""
        # 残差平方和
        rss = np.sum(residuals ** 2)
        
        # 均方误差
        mse = rss / n_samples
        
        # 对数似然 (假设误差服从正态分布)
        log_likelihood = -0.5 * n_samples * np.log(2 * np.pi * mse) - 0.5 * rss / mse
        
        # AIC (Akaike Information Criterion) - 惩罚参数数量
        aic = 2 * n_params - 2 * log_likelihood
        
        # BIC (Bayesian Information Criterion) - 更严格的惩罚
        bic = np.log(n_samples) * n_params - 2 * log_likelihood
        
        return aic, bic, log_likelihood
    
    def fit_models_with_regularization(self):
        """使用正则化拟合各种模型"""
        k_array = np.array(self.k_values)
        time_array = np.array(self.time_values)
        
        # 过滤掉第一个点（可能有启动开销）
        k_filtered = k_array[1:]
        time_filtered = time_array[1:]
        n_samples = len(k_filtered)
        
        models_to_fit = [
            ("O(1) 常数", self.constant_model, [1.0], 1),
            ("O(k) 线性", self.linear_model, [1e-6, 0], 2),
            ("O(log k) 对数", self.log_model, [1e-6, 0], 2),
            ("O(sqrt(k)) 平方根", self.sqrt_model, [1e-6, 0], 2),
            ("O(k log k) 对数线性", self.log_linear_model, [1e-9, 0], 2),
            ("O(k^b) 幂", self.power_model, [1e-12, 1, 0], 3)
        ]
        
        for name, model_func, initial_guess, n_params in models_to_fit:
            try:
                if name == "O(1) 常数":
                    # 对于常数模型，使用平均值
                    params = [np.mean(time_filtered)]
                    predicted = model_func(k_filtered, params[0])
                else:
                    # 拟合参数
                    popt, pcov = curve_fit(model_func, k_filtered, time_filtered, 
                                          p0=initial_guess, maxfev=5000)
                    params = popt
                    predicted = model_func(k_filtered, *params)
                
                # 计算拟合质量
                residuals = time_filtered - predicted
                ss_res = np.sum(residuals ** 2)
                ss_tot = np.sum((time_filtered - np.mean(time_filtered)) ** 2)
                r_squared = 1 - (ss_res / ss_tot)
                rmse = np.sqrt(np.mean(residuals ** 2))
                
                # 计算信息准则
                aic, bic, log_likelihood = self.calculate_information_criteria(
                    residuals, n_params, n_samples)
                
                self.models[name] = {
                    'function': model_func,
                    'params': params,
                    'r_squared': r_squared,
                    'rmse': rmse,
                    'aic': aic,
                    'bic': bic,
                    'log_likelihood': log_likelihood,
                    'predicted': predicted,
                    'n_params': n_params
                }
                
                print(f"\n{name} 拟合结果:")
                print(f"  参数: {params}")
                print(f"  R²: {r_squared:.6f}")
                print(f"  RMSE: {rmse:.6f}")
                print(f"  AIC: {aic:.2f} (参数数: {n_params})")
                print(f"  BIC: {bic:.2f} (更严格的惩罚)")
                
            except Exception as e:
                print(f"\n{name} 拟合失败: {e}")
    
    def select_best_model(self):
        """根据信息准则选择最佳模型"""
        print("\n" + "="*80)
        print("模型选择结果 (基于信息准则)")
        print("="*80)
        
        # 按AIC排序
        print("\n按 AIC 排序 (越小越好):")
        sorted_aic = sorted(self.models.items(), key=lambda x: x[1]['aic'])
        
        print(f"{'排名':<4} {'模型':<15} {'AIC':<10} {'BIC':<10} {'R²':<10} {'参数数':<6}")
        print("-" * 70)
        
        for rank, (name, model_info) in enumerate(sorted_aic, 1):
            print(f"{rank:<4} {name:<15} {model_info['aic']:<10.2f} "
                  f"{model_info['bic']:<10.2f} {model_info['r_squared']:<10.6f} "
                  f"{model_info['n_params']:<6}")
        
        # 按BIC排序
        print("\n按 BIC 排序 (越小越好，更严格):")
        sorted_bic = sorted(self.models.items(), key=lambda x: x[1]['bic'])
        
        best_aic = sorted_aic[0]
        best_bic = sorted_bic[0]
        
        print(f"\n🏆 AIC 最佳模型: {best_aic[0]}")
        print(f"   AIC = {best_aic[1]['aic']:.2f}")
        print(f"   R² = {best_aic[1]['r_squared']:.6f}")
        print(f"   参数数 = {best_aic[1]['n_params']}")
        
        print(f"\n🏆 BIC 最佳模型: {best_bic[0]}")
        print(f"   BIC = {best_bic[1]['bic']:.2f}")
        print(f"   R² = {best_bic[1]['r_squared']:.6f}")
        print(f"   参数数 = {best_bic[1]['n_params']}")
        
        # 特别关注 O(log k) 模型
        if 'O(log k) 对数' in self.models:
            log_model = self.models['O(log k) 对数']
            log_rank_aic = next((i for i, (name, _) in enumerate(sorted_aic, 1) if name == 'O(log k) 对数'), None)
            log_rank_bic = next((i for i, (name, _) in enumerate(sorted_bic, 1) if name == 'O(log k) 对数'), None)
            
            print(f"\n🎯 O(log k) 模型排名:")
            print(f"   AIC 排名: {log_rank_aic}/{len(sorted_aic)}")
            print(f"   BIC 排名: {log_rank_bic}/{len(sorted_bic)}")
            
            if log_rank_bic <= 2:
                print("   ✅ BIC 验证: O(log k) 是正确的模型选择!")
            elif log_rank_aic <= 2:
                print("   ⚠️  AIC 验证: O(log k) 是合理的模型选择!")
            else:
                print("   ❌ 需要进一步检查...")
        
        return best_aic[0], best_bic[0]
    
    def plot_results(self):
        """绘制拟合结果"""
        k_array = np.array(self.k_values)
        time_array = np.array(self.time_values)
        
        # 创建子图
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
        
        # 子图1: 原始数据和对数坐标
        ax1.loglog(k_array[1:], time_array[1:], 'bo-', label='实际数据', markersize=4)
        ax1.set_xlabel('k 值')
        ax1.set_ylabel('执行时间 (秒)')
        ax1.set_title('Pow(2, k, mod) 性能测试 - 对数坐标')
        ax1.grid(True, alpha=0.3)
        ax1.legend()
        
        # 子图2: 线性坐标显示前几个点
        k_small = k_array[1:6]
        time_small = time_array[1:6]
        ax2.plot(range(len(k_small)), time_small, 'ro-', label='实际数据', markersize=6)
        ax2.set_xlabel('测试序号')
        ax2.set_ylabel('执行时间 (秒)')
        ax2.set_title('Pow(2, k, mod) 性能测试 - 线性坐标 (前5个点)')
        ax2.grid(True, alpha=0.3)
        ax2.legend()
        
        # 子图3: 模型拟合比较 (重点显示 O(log k))
        k_filtered = k_array[1:]
        ax3.loglog(k_filtered, time_array[1:], 'bo-', label='实际数据', markersize=4)
        
        colors = ['red', 'green', 'orange', 'purple', 'brown', 'pink']
        important_models = ['O(log k) 对数', 'O(k^b) 幂', 'O(k) 线性']
        
        for i, model_name in enumerate(important_models):
            if model_name in self.models:
                model_info = self.models[model_name]
                color = colors[i % len(colors)]
                ax3.loglog(k_filtered, model_info['predicted'], 
                          color=color, linestyle='--', linewidth=2, 
                          label=f"{model_name} (R²={model_info['r_squared']:.3f}, "
                                f"AIC={model_info['aic']:.1f})")
        
        ax3.set_xlabel('k 值')
        ax3.set_ylabel('执行时间 (秒)')
        ax3.set_title('重点模型拟合比较 (含信息准则)')
        ax3.grid(True, alpha=0.3)
        ax3.legend()
        
        # 子图4: 信息准则比较
        model_names = list(self.models.keys())
        aic_values = [self.models[name]['aic'] for name in model_names]
        bic_values = [self.models[name]['bic'] for name in model_names]
        
        x_pos = np.arange(len(model_names))
        width = 0.35
        
        bars1 = ax4.bar(x_pos - width/2, aic_values, width, label='AIC', alpha=0.7)
        bars2 = ax4.bar(x_pos + width/2, bic_values, width, label='BIC', alpha=0.7)
        
        ax4.set_xlabel('模型')
        ax4.set_ylabel('信息准则值 (越小越好)')
        ax4.set_title('信息准则比较 (惩罚复杂模型)')
        ax4.set_xticks(x_pos)
        ax4.set_xticklabels(model_names, rotation=45, ha='right')
        ax4.legend()
        ax4.grid(True, alpha=0.3)
        
        # 标注最小值
        min_aic_idx = np.argmin(aic_values)
        min_bic_idx = np.argmin(bic_values)
        ax4.annotate('最小AIC', xy=(min_aic_idx - width/2, aic_values[min_aic_idx]), 
                    xytext=(10, 10), textcoords='offset points', 
                    arrowprops=dict(arrowstyle='->', color='blue'))
        ax4.annotate('最小BIC', xy=(min_bic_idx + width/2, bic_values[min_bic_idx]), 
                    xytext=(10, -10), textcoords='offset points', 
                    arrowprops=dict(arrowstyle='->', color='red'))
        
        plt.tight_layout()
        plt.savefig('/home/wuyankai/myResearch/新建文件夹/regularized_fitting.png', 
                   dpi=300, bbox_inches='tight')
        plt.show()

def main():
    """主函数"""
    print("带正则化的 Pow(2, k, mod) 性能拟合分析")
    print("="*60)
    print("使用 AIC/BIC 信息准则来惩罚复杂模型")
    print("="*60)
    
    # 创建拟合器实例
    fitter = RegularizedFitter()
    
    # 定义测试的k值（与原脚本相同）
    k_test_values = [
        10, 100, 1000, 10000, 100000, 1000000, 10000000, 
        100000000, 1000000000, 10000000000, 100000000000,
        1000000000000
    ]
    
    # 性能测试
    k_values, time_values = fitter.measure_pow_performance(k_test_values, iterations=10000)
    
    # 模型拟合
    fitter.fit_models_with_regularization()
    
    # 选择最佳模型
    best_aic, best_bic = fitter.select_best_model()
    
    # 生成图表
    fitter.plot_results()

if __name__ == "__main__":
    main()