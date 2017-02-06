import praw
import morse
import itertools
import traceback

reddit = praw.Reddit('morsebot');

def load_bot_footer():
    return open('bot_footer.md','r').read()

bot_footer = load_bot_footer();

num_replies = 0;
num_failed = 0;

for mention in itertools.ifilter(lambda x: x.new, reddit.inbox.mentions(limit = 10)):
    try:
        mention.refresh()
        parent = mention.parent()

        if isinstance(parent, praw.models.reddit.comment.Comment):
            parent_body = parent.body;
        elif isinstance(parent, praw.models.reddit.submission.Submission):
            parent_body = parent.selftext
        else:
            print "Unknown type of parent to mention: "
            print type(parent);
            print "Ignoring it...\n";
            num_failed = num_failed + 1
            continue;

        print "Mentioned by "+mention.author.name+' in response to "'+parent_body+'"';
        if "to-morse" in mention.body:
            print "Translating into Morse..."
            translation = morse.to_morse(parent_body);
        else:
            print "Translating from Morse..."
            translation = morse.to_latin(parent_body);
        print 'Replying with "'+translation+'"'
        mention.reply(translation + '\n' + bot_footer)
        mention.mark_read()
        num_replies = num_replies + 1
        print "Done.\n"
    except:
        traceback.print_exc();
        print "Failed to respond to mention from "+str(mention)+". Ignoring.\n"
        num_failed = num_failed+1;

if(num_replies is 0):
    print "No new mentions to reply to."
else:
    print "Replied to "+str(num_replies)+" mentions"

if(num_failed is not 0):
    print "Failed to reply to "+str(num_failed)+" mentions"
