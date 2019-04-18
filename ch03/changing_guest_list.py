names=['wu xue feng','guo peng','zhang lei','sun zhong hua']
invite_words=[' I ask you over for dinner tonight!',' I\'ll be glad to have you at mine for dinner tonight!',
' I\'m inviting you over for dinner tonight!',' I am inviting you to join me for dinner tonight!']
print(names[0].title()+invite_words[0])
print(names[1].title()+invite_words[1])
print(names[2].title()+invite_words[2])
print(names[3].title()+invite_words[3])
print('******************************')
unable_attend='wu xue feng'
#

print(unable_attend.title()+' unable to attend the dinner')
#replace the guest
names[0]='gou feng'

#invite everyone again
print('******************************')
print(names[0].title()+invite_words[0])
print(names[1].title()+invite_words[1])
print(names[2].title()+invite_words[2])
print(names[3].title()+invite_words[3])
