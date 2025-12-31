#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pow(2, k, mod) 性能拟合分析
分析 pow(2, k, mod) 的时间复杂度，并拟合多种模型
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

class PerformanceFitter:
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
    
    def fit_models(self):
        """拟合各种模型"""
        k_array = np.array(self.k_values)
        time_array = np.array(self.time_values)
        
        # 过滤掉第一个点（可能有启动开销）
        k_filtered = k_array[1:]
        time_filtered = time_array[1:]
        
        models_to_fit = [
            ("O(1) 常数", self.constant_model, [1.0]),
            ("O(k) 线性", self.linear_model, [1e-6, 0]),
            ("O(log k) 对数", self.log_model, [1e-6, 0]),
            ("O(sqrt(k)) 平方根", self.sqrt_model, [1e-6, 0]),
            ("O(k log k) 对数线性", self.log_linear_model, [1e-9, 0]),
            ("O(k^b) 幂", self.power_model, [1e-12, 1, 0])
        ]
        
        for name, model_func, initial_guess in models_to_fit:
            try:
                if name == "O(1) 常数":
                    # 对于常数模型，使用平均值
                    params = [np.mean(time_filtered)]
                else:
                    # 拟合参数
                    popt, _ = curve_fit(model_func, k_filtered, time_filtered, 
                                      p0=initial_guess, maxfev=5000)
                    params = popt
                
                # 计算拟合质量
                if name == "O(1) 常数":
                    predicted = model_func(k_filtered, params[0])
                else:
                    predicted = model_func(k_filtered, *params)
                
                # 计算R²和RMSE
                ss_res = np.sum((time_filtered - predicted) ** 2)
                ss_tot = np.sum((time_filtered - np.mean(time_filtered)) ** 2)
                r_squared = 1 - (ss_res / ss_tot)
                rmse = np.sqrt(np.mean((time_filtered - predicted) ** 2))
                
                self.models[name] = {
                    'function': model_func,
                    'params': params,
                    'r_squared': r_squared,
                    'rmse': rmse,
                    'predicted': predicted
                }
                
                print(f"\n{name} 拟合结果:")
                print(f"  参数: {params}")
                print(f"  R²: {r_squared:.6f}")
                print(f"  RMSE: {rmse:.6f}")
                
            except Exception as e:
                print(f"\n{name} 拟合失败: {e}")
    
    def plot_results(self):
        """绘制拟合结果"""
        k_array = np.array(self.k_values)
        time_array = np.array(self.time_values)
        
        # 创建子图
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
        
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
        
        # 子图3: 模型拟合比较
        k_filtered = k_array[1:]
        ax3.loglog(k_filtered, time_array[1:], 'bo-', label='实际数据', markersize=4)
        
        colors = ['red', 'green', 'orange', 'purple', 'brown', 'pink']
        for i, (name, model_info) in enumerate(self.models.items()):
            if len(model_info['predicted']) > 0:
                ax3.loglog(k_filtered, model_info['predicted'], 
                          color=colors[i % len(colors)], 
                          linestyle='--', linewidth=2, 
                          label=f"{name} (R²={model_info['r_squared']:.3f})")
        
        ax3.set_xlabel('k 值')
        ax3.set_ylabel('执行时间 (秒)')
        ax3.set_title('模型拟合比较')
        ax3.grid(True, alpha=0.3)
        ax3.legend()
        
        # 子图4: 残差分析
        if 'O(log k) 对数' in self.models:
            best_model = self.models['O(log k) 对数']
            residuals = time_array[1:] - best_model['predicted']
            ax4.semilogx(k_filtered, residuals, 'go-', markersize=4)
            ax4.axhline(y=0, color='red', linestyle='--', alpha=0.7)
            ax4.set_xlabel('k 值')
            ax4.set_ylabel('残差 (实际值 - 预测值)')
            ax4.set_title('O(log k) 模型残差分析')
            ax4.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('/home/wuyankai/myResearch/新建文件夹/performance_fitting.png', 
                   dpi=300, bbox_inches='tight')
        plt.show()
    
    def print_summary(self):
        """打印拟合总结"""
        print("\n" + "="*60)
        print("Pow(2, k, mod) 时间复杂度拟合总结")
        print("="*60)
        
        # 按R²排序
        sorted_models = sorted(self.models.items(), 
                             key=lambda x: x[1]['r_squared'], 
                             reverse=True)
        
        print(f"{'排名':<4} {'模型':<15} {'R²':<10} {'RMSE':<12} {'参数'}")
        print("-" * 60)
        
        for rank, (name, model_info) in enumerate(sorted_models, 1):
            params_str = ', '.join([f"{p:.6e}" for p in model_info['params']])
            print(f"{rank:<4} {name:<15} {model_info['r_squared']:<10.6f} "
                  f"{model_info['rmse']:<12.6e} [{params_str}]")
        
        print("\n结论:")
        best_model = sorted_models[0]
        print(f"最佳拟合模型: {best_model[0]}")
        print(f"拟合质量 (R²): {best_model[1]['r_squared']:.6f}")
        
        if 'O(log k)' in best_model[0]:
            print("验证了 pow(2, k, mod) 的时间复杂度确实是 O(log k)")
            print("这与快速幂算法的理论分析一致")
        elif best_model[1]['r_squared'] > 0.8:
            print("拟合效果良好")
        else:
            print("建议检查测试数据或模型选择")

def main():
    """主函数"""
    print("Pow(2, k, mod) 性能拟合分析")
    print("="*50)
    
    # 创建拟合器实例
    fitter = PerformanceFitter()
    
    # 定义测试的k值（与原脚本相同）
    k_test_values = [
        10, 100, 1000, 10000, 100000, 1000000, 10000000, 
        100000000, 1000000000, 10000000000, 100000000000,
        1000000000000, 10000000000000, 100000000000000,
        1000000000000000, 10000000000000000, 
        100000000000000000, 1000000000000000000,
        10000000000000000000
    ]
    
    # 性能测试
    k_values, time_values = fitter.measure_pow_performance(k_test_values, iterations=10000)
    
    # 模型拟合
    fitter.fit_models()
    
    # 生成图表
    fitter.plot_results()
    
    # 打印总结
    fitter.print_summary()

if __name__ == "__main__":
    main()