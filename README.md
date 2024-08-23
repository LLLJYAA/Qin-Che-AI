# Qin-Che-AI
Here's a simple and user-friendly `README.md` template that you can use to guide beginners on how to run your AI assistant program. The instructions are clear and step-by-step to ensure even those with minimal technical knowledge can follow along.

---

# 秦彻 AI 助手

这个项目是一个基于 OpenAI API 的互动式终端助手，扮演角色秦彻，与你（猎人小姐）进行对话。

## 特点
- 扮演角色：秦彻，暗点组织的首领，与你（猎人小姐）进行互动。
- 主线情节：用久候狂欢之徒主线进行训练，较为符合低好感度秦彻的性格风格。
- 动态对话：根据你的输入，秦彻会做出不同的反应，并显示出他独特的个性。
- 记忆功能：秦彻会记住你们之间的对话，逐步推进情感交流。

## 安装和运行步骤

### 第一步：安装 Python 和依赖库

1. **安装 Python**:
    - 如果你还没有安装 Python，请前往[Python 官方网站](https://www.python.org/)下载并安装最新版本。

2. **安装依赖库**:
    - 打开命令提示符或终端，输入以下命令来安装所需的库：
      ```bash
      pip install openai
      ```
   - 如果出现报错： 'pip' 不是内部或外部命令，也不是可运行的程序或批处理文件。
     那么需要将 Python 添加到系统环境变量中：
     右键点击桌面上的 “此电脑” 或 “计算机” 图标，然后选择 “属性”。
     在弹出的窗口中，点击左侧的 “高级系统设置”。
     在 “系统属性” 窗口中，点击 “环境变量” 按钮。

### 第二步：获取 OpenAI API 密钥

1. **注册 OpenAI 账号**:
    - 前往[OpenAI 网站](https://beta.openai.com/signup/)注册一个账号。

2. **获取 API 密钥**:
    - 登录后，进入[API 密钥页面](https://platform.openai.com/account/api-keys)并生成一个新的密钥。复制这个密钥，稍后会用到。

### 第三步：配置和运行程序

1. **下载代码**:
    - 将本项目代码下载到你的电脑。
    - 在项目页面的右侧，你会看到一个绿色的 Code 按钮，点击它并选择 Download ZIP。
![image](https://github.com/user-attachments/assets/d75e0573-3624-4ccc-8916-85b3d8f0b101)
    - 下载完成后解压zip文件，找到test.py，用你喜欢的文本编辑器（如 VSCode、Notepad++、记事本 等）打开



2. **修改 API 密钥**:
    - 在代码中，找到以下行，并将 `"your-api-key-here"` 替换为你在上一步获取的 API 密钥：
      ```python
      client = OpenAI(api_key="your-api-key-here")
      ```
      例如：
      ```python
      client = OpenAI(api_key="sk-proj-H3123123123123-gj7")
      ```

3. **运行程序**:
    - 双击启动 test.py
    - 程序启动后，你将看到提示 `猎人小姐:`，你可以在这里输入你的问题或对话，秦彻将会回应你。

### 第四步：与秦彻互动

- **输入消息**: 在终端中输入你的问题或对话，按下回车键，秦彻会根据他的性格和设定回应你。
- **退出程序**: 如果你想结束对话，只需输入 `exit` 并按回车。

## 项目结构

- `test.py` - 主程序文件，包含了秦彻 AI 助手的逻辑。
- `README.md` - 当前文件，提供项目介绍和使用说明。

### 第五步：调整模型
#### 调整秦彻的性格和对话风格
在代码的系统消息中，你定义了秦彻的角色和性格描述。你可以根据需要修改引号内的这些中文内容，以调整秦彻的对话风格和行为：

```python
messages = [
    {"role": "system", "content": "你扮演的是秦彻, ..."}  # 这里的描述定义了秦彻的性格
]
```
#### 调整 `temperature` 参数

- **作用**: `temperature` 参数控制模型生成文本的随机性。较低的值（如 0.2）会使输出更加确定和一致，而较高的值（如 0.8 或 1.0）会使生成的文本更有创意和随机性。
- **调整方法**: 如果你想让秦彻的回应更加不确定和多变，可以增加 `temperature` 的值；如果想要他更加冷静和严谨，可以降低这个值。

```python
# 例如，将 temperature 从 0.85 调整为 0.6，使秦彻更冷静
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    temperature=0.6  # 更冷静的对话
)
```


## 贡献

欢迎提交 Pull Request 来改进这个项目。如果你有任何建议或问题，请在 GitHub 上创建 Issue。


