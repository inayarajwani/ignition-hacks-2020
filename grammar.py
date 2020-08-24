import jdk
import language_check
tool = language_check.LanguageTool('en-US')
text = (input ("enter text to check the grammar: "))
matches = tool.check(text)
len(matches)
