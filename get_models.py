import pickle
fn=['dtca856d21woph.pkl', 'dtca857d18woph.pkl',
    'dtca924d19ph.pkl', 'dtca926d18ph.pkl',
    'nbctr854te87wopH.pkl',
    'nbctr933te94withpH.pkl',
    'rfcte884tr1wopH.pkl', 'rfcte886tr1wopH.pkl',
    'rfcte944tr1withpH.pkl', 'rfcte946tr1withpH.pkl', 'rfcte953tr1withpH.pkl']
def c_fn(ufn):
  return 'mlm/'+ufn
fn=list(map(c_fn,fn))
def grab():
  dtph=[]
  dtwoph=[]
  rfcph=[]
  rfcwoph=[]
  nbcph=pickle.load(open(fn[5],'rb'))
  nbcwoph=pickle.load(open(fn[4],'rb'))
  for i in fn[0:2]:
      t23 = pickle.load(open(i,'rb'))
      dtwoph.append(t23)
  for i in fn[2:4]:
      t23 = pickle.load(open(i,'rb'))
      dtph.append(t23)
  for i in fn[6:8]:
      t23 = pickle.load(open(i,'rb'))
      rfcwoph.append(t23)
  for i in fn[8:11]:
      t23 = pickle.load(open(i,'rb'))
      rfcph.append(t23)
  return [dtph,nbcph,rfcph],[dtwoph,nbcwoph,rfcwoph]    
