{
  "rewrite_specs": [
    {
      "id": "input_1",
      "pattern": "n\\s*,\\s*m\\s*=\\s*map\\(int,\\s*input\\(\\)\\.split\\(\\)\\)",
      "variables": [
        { "name": "n", "scale_with_n": true },
        { "name": "m", "scale_with_n": false, "default": 1 }
      ],
      "replacement_template": "n, m = {n}, {m}"
    },
    {
      "id": "input_2",
      "pattern": "arr\\s*=\\s*list\\(map\\(int,\\s*input\\(\\)\\.split\\(\\)\\)\\)",
      "variables": [
        { "name": "arr", "scale_with_n": true, "generator": "list_int" }
      ],
      "replacement_template": "arr = {arr}"
    }，
    {
  "id": "loop_input_x",
  "type": "loop_input",
  "pattern": "for\\s+_\\s+in\\s+range\\(n\\):\\s*\\n\\s*x\\s*=\\s*int\\(input\\(\\)\\)",
  "loop_var": "n",
  "variables": [
    {
      "name": "x",
      "dtype": "int"
    }
  ],
  "replacement_template": [
    "for _ in range({n}):",
    "    x = 1"
  ]
}
  ]
}