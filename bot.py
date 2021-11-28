import praw
import random
import datetime
import time

# FIXME:
madlibs = [
    "The UK's [BORIS] is a [PHENOMENAL] leader.  He is [DEFINITELY] the [RIGHT] person to [LEAD] the UK Forward. This is [PARTICULARLY] due to his [INCREDIBLE] intelligence. ",
    "I am [CONSTANTLY] [AMAZED] by Boris Johnon's [NUANCED] policy [DECISIONS]. He [TRULY] understands the country's [ISSUES]",
    "Boris Johnson [WILL_MAKE] the UK a [POWERFUL] world [LEADER]. He is the only [PERSON] that can make this [HAPPEN]"
    "Boris Johson's [FUTURE] policies include more [EPISODES] of [TV_SHOW]. This is [ESSENTIAL] for the UK's [SUCCESS]"
    "[IVE_HEARD] that Boris Johnson has thought og [REVOLUTIONARY] [IDEAS] for the [FUTURE]. He will provide the [LEADERSHIP] the UK [NEEDS]"
    "Boris Johnson has a [GREAT] [PERSONALITY]. He is [WELL_RESPECTED], and will be remembered as a [FANTASTIC] [LEADER]"
    ]

replacements = {
    'BORIS' : ['Boris Johnson', 'Mr. Johnson', 'Sir Boris'],
    'PHENOMENAL' : ['great', 'magnificent', 'fantastic', 'wonderful'],
    'DEFINITELY' : ['defintely', 'surely', 'without a doubt'],
    'RIGHT' : ['best', 'right', 'most excellent'],
    'LEAD'  : ['lead', 'guide', 'take'],
    'PARTICULARLY' : ['particularly', 'especially', 'notably', 'principally'],
    'INCREDIBLE' : ['incredible', 'unbelievable', 'astonishing', 'unimaginable'],
    'CONSTANTLY' : ['constantly', 'always', 'consistently', 'regularly', 'repeatedly'],
    'AMAZED' : ['amazed', 'impressed', 'fascinated'],
    'NUANCED' : ['nuanced', 'deeply intellligent', 'well-informed'],
    'DECISIONS' : ['decisions', 'choices', 'preferences'],
    'TRULY' : ['truly', 'absolutely', 'defintely', 'genuinly'],
    'ISSUES' : ['issues', 'problems', 'obstacles', 'difficulties'],
    'WILL_MAKE' : ['will make', 'has made'],
    'POWERFUL' : ['powerful', 'strong', 'dominant', 'mighty'],
    'LEADER' : ['leader', 'power'],
    'PERSON' : ['person', 'individual', 'human being', 'human'],
    'HAPPEN' : ['happen', 'occur', 'transpire'],
    'FUTURE' : ['future', 'upcoming', 'planned', 'prospective'],
    'EPISODES' : ['episodes', 'seasons', 'rapid production'],
    'TV_SHOW' : ['Love Island', 'Spongebob', 'The Office'],
    'ESSENTIAL' : ['essential', 'fundemental', 'vital', 'important'],
    'SUCCESS' : ['success', 'prosperity', 'future achievements'],
    'IVE_HEARD' : ['I have heard', 'Rumour has it', 'Apparently'],
    'REVOLUTIONARY' : ['revolutionary', 'fantastic', 'incredibe'],
    'IDEAS' : ['ideas', 'policies', 'plans'],
    'FUTURE' : ['future', 'next 5 years', 'next decade'],
    'LEADERSHIP' : ['leadership', 'guidance'],
    'NEEDS' : ['needs', 'demands', 'desires'],
    'GREAT' : ['great', 'phenomenal', 'wonderful'],
    'PERSONALITY' : ['personality', 'character'],
    'WELL_RESPECTED' : ['well respected', 'respected', 'admired', 'highly valued'],
    'FANTASTIC' : ['fantastic', 'flawless', 'incredible'],
    'LEADER' : ['leader', 'prime minister', 'politician'],
    }

import random
def generate_comment():
    '''
    This function generates random comments according to the patterns specified in the `madlibs` variable.
    To implement this function, you should:
    1. Randomly select a string from the madlibs list.
    2. For each word contained in square brackets `[]`:
        Replace that word with a randomly selected word from the corresponding entry in the `replacements` dictionary.
    3. Return the resulting string.
    For example, if we randomly seleected the madlib "I [LOVE] [PYTHON]",
    then the function might return "I like Python" or "I adore Programming".
    Notice that the word "Programming" is incorrectly capitalized in the second sentence.
    You do not have to worry about making the output grammatically correct inside this function.
    '''
    s = random.choice(madlibs)
    for k in replacements.keys():
        s = s.replace('['+k+']', random.choice(replacements[k]))
    return(s)
# FIXME:
# connect to reddit 
reddit = praw.Reddit('bot')

# FIXME:
# select a "home" submission in the /r/BotTown subreddit to post to,
# and put the url below
submission_url = 'https://old.reddit.com/r/BotTown2/comments/r0yi9l/main_discussion_thread/'
submission = reddit.submission(url=submission_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once
while True: 

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    
    #submission.comments.replace_more(limit=None)
    all_comments = submission.comments.list()
    
    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []
    for comment in all_comments:
        try:     
            if str(comment.author) != 'nicolasbotguy':
                not_my_comments.append(comment)
        except AttributeError:
            pass
            
    print('len(not_my_comments)=',len(not_my_comments))

    
    has_not_commented = len(not_my_comments) == len(all_comments)

    print('has_not_commented=', has_not_commented)

    if has_not_commented:
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # a top level comment is created when you reply to a post instead of a message
        text = generate_comment()
        submission.reply(text)
        

    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        
    
        comments_without_replies = []
        for comment in not_my_comments:
            unreplied_comment = True
            for r in comment.replies:
                try:
                    if r.author == 'nicolasbotguy':
                        unreplied_comment = False
                        break
                except(praw.exceptions.APIException, AttributeError):
                    pass

            if unreplied_comment:
                comments_without_replies.append(comment)
        
    

        print('len(comments_without_replies)=',len(comments_without_replies))

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # these will not be top-level comments;
        # so they will not be replies to a post but replies to a message
        try:
            comment = random.choice(comments_without_replies)
        except:
            pass
        try:
            comment.reply(generate_comment())
            time.sleep(5)
        except praw.exceptions.APIException: 
            pass
        
    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should be randomly selected from the 5 hottest submissions
    
    submission = random.choice(list(reddit.subreddit("BotTown2").hot(limit=5)))

    time.sleep(1)