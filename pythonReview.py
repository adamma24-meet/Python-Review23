

def creat_youtube_video(title,description):
	likes=0
	dislike=0
	username=""
	comment=""

	comments={}
	videos={'Title':title,'Description':description,'Likes':likes,'Dislike':dislike,'comments': comments}
	return videos

def like(x):
	if "Likes" in x:
		x['Likes']+=1
		return x

def dislike(y):
	if "Dislike" in y:
		y['Dislike']+=1
	return y

def add_comment(youtubevideo,username,comment_text):
	youtubevideo['comments'][username]=comment_text

test =creat_youtube_video('adam','who is adam')

like(test)
dislike(test)
add_comment(test,'galegor the destroyer','i am fatter')
print(test)

		




	


