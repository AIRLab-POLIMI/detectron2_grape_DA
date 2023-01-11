
import json
import matplotlib.pyplot as plt

experiment_folder = './RGB_MaskRCNN_SFT2J_wgisd_output'

def load_json_arr(json_path):
    lines = []
    with open(json_path, 'r') as f:
        for line in f:
            lines.append(json.loads(line))
    return lines

experiment_metrics = load_json_arr(experiment_folder + '/metrics.json')
iters_total_loss = [x['iteration'] for x in experiment_metrics if 'total_loss' in x]
total_loss = [x['total_loss'] for x in experiment_metrics if 'total_loss' in x]

fig, ax = plt.subplots()
ax.plot(iters_total_loss, total_loss)
#ax.plot(iters_val_loss, val_loss)
ax.set_xlabel('iteration')
ax.set_ylabel('loss')
#ax.legend(['total_loss', 'validation_loss'], loc='best')
ax.set_title('training_loss')
#ax.legend(['total_loss'], loc='best')
#iter = val_loss.index(min(val_loss))
iter_ = total_loss.index(min(total_loss))
ax.vlines(iters_total_loss[iter_], 0, float(max(total_loss)),color="red")
ax.annotate('min loss: %f at iter: %d'%(float(min(total_loss)),int(iters_total_loss[iter_])),xy=(iters_total_loss[iter_],min(total_loss)),\
        xytext=(+15,+15),textcoords='offset points',fontsize=8) 
ax.set_xlim([0,max(iters_total_loss)])
ax.set_ylim([0,4.0])

#plt.show()
path = '../data/'+experiment_folder+'_training_loss.jpg' #experiment_folder + '/loss.jpg'
plt.savefig(path)
plt.close()
