from flask import Flask, render_template, url_for, request, redirect
import os, os.path
import json

ip_address = "155.69.146.170"

app = Flask(__name__)
dataset = json.load(open('merged_results.json'))
cap_LBDs = dataset['LBD_result']
cap_RFEs = dataset['RFE_result']
cap_GRTs = dataset['GRT_result']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/redirect_user')
def redirect_user():
    for uid in range(0,20):
        user_result_dir = './users/u%d/result/'%uid
        if not os.path.exists('./users/u%d/'%(uid)):
            os.system('mkdir ./users/u%d/'%(uid))
            os.system('mkdir ./users/u%d/result/'%(uid))
            os.system('python ./pick_data.py')
            os.system('cp ./cap_data/im_c_list.json ./users/u%d/'%(uid))
            os.system('cp ./new_im_q.json ./users/u%d/im_q_list.json'%(uid))
            
        if len(os.listdir(user_result_dir))==0 and not os.path.exists('./users/u%d/on_hold.json'%(uid)):
            with open('./users/u%d/on_hold.json'%(uid), 'w') as outfile:
                json.dump([1], outfile)
            return redirect('http://'+ ip_address +':5000/%d'%uid)
    return redirect('http://' + ip_address + ':5000/thanks')

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

@app.route('/<int:uid>', methods=['GET', 'POST'])

def start(uid):
    im_q_list = json.load(open('./users/u%d/im_q_list.json' % (uid)))
    if request.method == 'POST':
        print('saving --- ')
        fluent = request.form['fluent']
        correct = request.form['correct']
        fluent_u = request.form['fluent_u']
        correct_u = request.form['correct_u']
        fluent_g = request.form['fluent_g']
        correct_g = request.form['correct_g']
        imid = request.form['imid']
        qid = request.form['qid']
        question_type = request.form['question_type']
        print('<%s,%s,%s>'%(imid,qid,question_type))
        result = {'imid': int(imid), 'qid': int(qid), 'fluent_score': int(fluent), 'correct_score': int(correct),
                  'fluent_score_u': int(fluent_u), 'correct_score_u': int(correct_u),
                  'fluent_score_g': int(fluent_g), 'correct_score_g': int(correct_g)}
        print('./users/u%d/result/%d_%d.json' % (uid, int(imid), int(qid)))
        with open('./users/u%d/result/%d_%d.json'%(uid,int(imid),int(qid)), 'w') as outfile:
            json.dump(result, outfile)

        print(request.form)

    user_result_dir = './users/u%d/result/'%uid
    postid = len(os.listdir(user_result_dir))
    print(postid)
    if postid==len(im_q_list):
        return redirect('http://' + ip_address + ':5000/thanks')
    print('loading --- ')
    imid =im_q_list[postid][0]
    qid = im_q_list[postid][1]
    #img_folder = 'static/cocodata'
    imfile  = r'static/videos/video%s.mp4'%(str(imid))
    cap_LBD = cap_LBDs[imid]
    cap_RFE = cap_RFEs[imid]
    cap_GRT = cap_GRTs[imid][qid]
    question = "I do not know what is the question!"
    question_type = "None!"
    answer = "I do not know anything about the answer!"
    print(imid,cap_LBD,cap_RFE,cap_GRT)
    print('uid--', uid)
    prog = int(float(postid)/len(im_q_list)*100)
    print('prog--',prog)
    return render_template('start.html',imfile=imfile, question=question,
    answer=answer,explanation=cap_LBD,explanation_u=cap_RFE, explanation_g=cap_GRT, imid=imid,qid=qid,postid=postid,question_type=0,prog=0)
