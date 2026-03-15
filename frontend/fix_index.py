import re

with open('index.html', 'r') as f:
    content = f.read()

# 修改模板：为每个 project-card 添加 data 属性和新结构
# 注意：这会将所有卡片的描述替换为结构模板，你需要手动填入实际数据

# 1. 在 data-diff 后添加 data-tech 和 data-price 属性（示例值，你需要根据实际项目修改）
content = content.replace(
    'data-diff="局部修复"><div class="p-5">',
    'data-diff="局部修复" data-tech="React,Node.js" data-price="5000"><div class="p-5">'
)

# 2. 在描述段落前添加技术栈标签区域
old_desc = '<p class="text-slate-400 text-sm mb-4 line-clamp-2">'
new_structure = '''<div class="flex gap-1 flex-wrap mb-2 tech-tags">
                    <span class="px-2 py-0.5 bg-slate-700 text-xs rounded text-slate-300">React</span>
                    <span class="px-2 py-0.5 bg-slate-700 text-xs rounded text-slate-300">Node.js</span>
                </div>
                <p class="text-slate-400 text-sm mb-3 line-clamp-2 font-medium text-emerald-400/80">'''
content = content.replace(old_desc, new_structure, 1)  # 只改第一个作为示例

# 3. 在卡片结尾前添加价格区域
old_end = '</p></div></div>'
new_end = '''</p>
                <div class="flex justify-between items-center mt-3 pt-3 border-t border-slate-700/50">
                    <span class="text-emerald-400 font-bold text-sm">¥5,000</span>
                    <span class="text-xs text-slate-500">点击查看详情</span>
                </div>
            </div>
        </div>'''
content = content.replace(old_end, new_end, 1)

with open('index.html', 'w') as f:
    f.write(content)

print("✅ 已修改第一个卡片作为模板，请参照修改其余卡片")
