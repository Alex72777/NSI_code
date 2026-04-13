import wikipedia

wikipedia.set_lang('fr')
wikipedia.set_user_agent("firefox")
page = wikipedia.page('wikipedia')
print(page.summary[:])