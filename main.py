from browser import document, alert

def Formatter(event):
  code = document['input-area'].value
  FC = ""
  
  for i in code:
    if i == "<":
      FC += "&lt;"
    elif i == ">":
      FC += "&gt;"
    elif i == "&":
      FC += "&amp;"
    elif i == "\n":
      FC += "<br>"
    else:
      FC += i
  
  document['output-area'].text = FC
  
document['submit-button'].bind('click', Formatter)

def copier(event):
  FormattedElement = document['output-area']
  FormattedElement.select()
  document.execCommand('copy')
  alert('Formatted Code Copied!')
document['output-area'].bind('focus', copier)
