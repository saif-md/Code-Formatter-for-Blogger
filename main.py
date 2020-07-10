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
  if document['output-area'].value != '':
    FormattedElement = document['output-area']
    FormattedElement.select()
    document.execCommand('copy')
    alert('Formatted Code Copied!')
  else:
    alert('First put your code in the input box please.')
document['output-area'].bind('click', copier)
