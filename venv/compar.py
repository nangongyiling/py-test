import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from wordcloud import WordCloud
from scipy.misc import imread
import jieba
from pylab import mpl

# 使matplotlib模块能显示中文
#mpl.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

# 读取数据
df = pd.read_csv('lagou.csv', encoding='utf-8')
# 数据清洗,剔除实习岗位
df.drop(df[df['职位名称'].str.contains('实习')].index, inplace=True)
# print(df.describe())
# 由于CSV文件内的数据是字符串形式,先用正则表达式将字符串转化为列表,再取区间的均值
pattern = '\d+'
df['work_year'] = df['工作经验'].str.findall(pattern)
# 数据处理后的工作年限
avg_work_year = []
# 工作年限
for i in df['work_year']:
   # 如果工作经验为'不限'或'应届毕业生',那么匹配值为空,工作年限为0
   if len(i) == 0:
       avg_work_year.append(0)
   # 如果匹配值为一个数值,那么返回该数值
   elif len(i) == 1:
       avg_work_year.append(int(''.join(i)))
   # 如果匹配值为一个区间,那么取平均值
   else:
       num_list = [int(j) for j in i]
       avg_year = sum(num_list)/2
       avg_work_year.append(avg_year)
df['工作经验'] = avg_work_year

# 将字符串转化为列表,再取区间的前25%，比较贴近现实
df['salary'] = df['工资'].str.findall(pattern)
# 月薪
avg_salary = []
for k in df['salary']:
   int_list = [int(n) for n in k]
   avg_wage = int_list[0]+(int_list[1]-int_list[0])/4
   avg_salary.append(avg_wage)
df['月工资'] = avg_salary

# # 将清洗后的数据保存,以便检查
# df.to_csv('draft.csv', index = False)

# 描述统计
#print('Python开发工资描述：\n{}'.format(df['月工资'].describe()))


# 绘制频率直方图并保存
plt.hist(df['月工资'])
plt.xlabel('工资 (千元)')
plt.ylabel('频数')
plt.title("工资直方图")
plt.savefig('histogram.jpg')
plt.show()


# 实证统计,将学历不限的职位要求认定为最低学历:大专\
df['学历要求'] = df['学历要求'].replace('不限','大专')

# {'本科': 1304, '大专': 94, '硕士': 57, '博士': 1}
dict = {}
for i in df['学历要求']:
    if i not in dict.keys():
        dict[i] = 0
    else:
        dict[i] += 1
index = list(dict.keys())
print(index)
num = []
for i in  index:
    num.append(dict[i])
print(num)
plt.bar(left=index, height=num, width=0.5)
plt.show()

# 绘制饼图并保存
count = df['区域'].value_counts()
plt.pie(count, labels = count.keys(),labeldistance=1.4,autopct='%2.1f%%')
plt.axis('equal')  # 使饼图为正圆形
plt.legend(loc='upper left', bbox_to_anchor=(-0.1, 1))
plt.savefig('pie_chart.jpg')
plt.show()

# 绘制词云,将职位福利中的字符串汇总
text = ''
for line in df['职位福利']:
   text += line
# 使用jieba模块将字符串分割为单词列表
cut_text = ' '.join(jieba.cut(text))
#color_mask = imread('cloud.jpg')  #设置背景图
cloud = WordCloud(
    background_color = 'white',
    # 对中文操作必须指明字体
    font_path='yahei.ttf',
    #mask = color_mask,
    max_words = 1000,
    max_font_size = 100
    ).generate(cut_text)

# 保存词云图片
cloud.to_file('word_cloud.jpg')
plt.imshow(cloud)
plt.axis('off')
plt.show()
# word_cloud = cloud.generate(cut_text)
# 保存词云图片
cloud.to_file('word_cloud.jpg')
plt.imshow(cloud)
plt.axis('off')


