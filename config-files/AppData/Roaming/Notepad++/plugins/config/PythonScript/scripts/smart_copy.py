if len(editor.getSelText()) > 0:
    editor.copy()
else:
    editor.copyText(editor.getCurLine())
