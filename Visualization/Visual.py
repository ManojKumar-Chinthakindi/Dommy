import self

from Data_Insertion.EDA_Process import df
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()


class plots:

    try:

        def __init__(self, dist_pl, dist_se, dist_cp, dist_tr, dist_ch, dist_fb, dist_re, dist_th, dist_ex, dist_ol, dist_sl, dist_ca, dist_tl, dist_tt, scatter_pl, scatter_se, scatter_cp, scatter_tr, scatter_ch, scatter_fb, scatter_re, scatter_th, scatter_ex, scatter_ol, scatter_sl, scatter_ca, scatter_tl, scatter_tt, age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, target):
            self.dist_pl = dist_pl
            self.dist_se = dist_se
            self.dist_cp = dist_cp
            self.dist_tr = dist_tr
            self.dist_ch = dist_ch
            self.dist_fb = dist_fb
            self.dist_re = dist_re
            self.dist_th = dist_th
            self.dist_ex = dist_ex
            self.dist_ol = dist_ol
            self.dist_sl = dist_sl
            self.dist_ca = dist_ca
            self.dist_tl = dist_tl
            self.dist_tt = dist_tt
            self.scatter_pl = scatter_pl
            self.scatter_se = scatter_se
            self.scatter_cp = scatter_cp
            self.scatter_tr = scatter_tr
            self.scatter_ch = scatter_ch
            self.scatter_fb = scatter_fb
            self.scatter_re = scatter_re
            self.scatter_th = scatter_th
            self.scatter_ex = scatter_ex
            self.scatter_ol = scatter_ol
            self.scatter_sl = scatter_sl
            self.scatter_ca = scatter_ca
            self.scatter_tl = scatter_tl
            self.scatter_tt = scatter_tt
            self.age = age
            self.sex = sex
            self.cp = cp
            self.trestbps = trestbps
            self.chol = chol
            self.fbs = fbs
            self.restecg = restecg
            self.thalach = thalach
            self.exang = exang
            self.oldpeak = oldpeak
            self.slope = slope
            self.ca = ca
            self.thal = thal
            self.target = target

        def dist_pl(self):
            plt.subplots(figsize=(5, 5))
            sns.distplot(df['age'], color='red')
            plt.legend('Age on Heart Disease')
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\dist_pl.PNG')
            plt.show()

        dist_pl(self)

        def dist_se(self):
            plt.subplots(figsize=(5, 5))
            sns.distplot(df['sex'],color='red')
            plt.legend('Sex on Heart Disease')
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\dist_se.PNG')
            plt.show()
        dist_se(self)

        def dist_cp(self):
            plt.subplots(figsize=(5, 5))
            sns.distplot(df['cp'],color='red')
            plt.legend('cp on Heart Disease')
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\dist_cp.PNG')
            plt.show()
        dist_cp(self)


        def dist_tr(self):
            plt.subplots(figsize=(5, 5))
            sns.distplot(df['trestbps'],color='red')
            plt.legend('trestbps on Heart Disease')
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\dist_tr.PNG')
            plt.show()
        dist_tr(self)

        def dist_ch(self):
            plt.subplots(figsize=(5, 5))
            sns.distplot(df['chol'],color='red')
            plt.legend('chol on Heart Disease')
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\dist_ch.PNG')
            plt.show()
        dist_ch(self)

        def dist_fb(self):
            plt.subplots(figsize=(5, 5))
            sns.distplot(df['fbs'],color='red')
            plt.legend('fbs on Heart Disease')
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\dist_fb.PNG')
            plt.show()
        dist_fb(self)


        def dist_re(self):
            plt.subplots(figsize=(5, 5))
            sns.distplot(df['restecg'],color='red')
            plt.legend('restecg on Heart Disease')
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\dist_re.PNG')
            plt.show()
        dist_re(self)



        def dist_th(self):
            plt.subplots(figsize=(5, 5))
            sns.distplot(df['thalach'],color='red')
            plt.legend('thalach on Heart Disease')
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\dist_th.PNG')
            plt.show()
        dist_th(self)



        def dist_ex(self):
            plt.subplots(figsize=(5, 5))
            sns.distplot(df['exang'],color='red')
            plt.legend('exang on Heart Disease')
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\dist_ex.PNG')
            plt.show()
        dist_ex(self)



        def dist_ol(self):
            plt.subplots(figsize=(5, 5))
            sns.distplot(df['oldpeak'],color='red')
            plt.legend('oldpeak on Heart Disease')
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\dist_ol.PNG')
            plt.show()
        dist_ol(self)



        def dist_sl(self):
            plt.subplots(figsize=(5, 5))
            sns.distplot(df['slope'],color='red')
            plt.legend('slope on Heart Disease')
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\dist_sl.PNG')
            plt.show()
        dist_sl(self)



        def dist_ca(self):
            plt.subplots(figsize=(5, 5))
            sns.distplot(df['ca'],color='red')
            plt.legend('ca on Heart Disease')
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\dist_ca.PNG')
            plt.show()
        dist_ca(self)


        def dist_tl(self):
            plt.subplots(figsize=(5, 5))
            sns.distplot(df['thal'],color='red')
            plt.legend('thal on Heart Disease')
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\dist_tl.PNG')
            plt.show()
        dist_tl(self)


        def dist_tt(self):
            plt.subplots(figsize=(5, 5))
            sns.distplot(df['target'],color='red')
            plt.legend('target on Heart Disease')
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\dist_tt.PNG')
            plt.show()
        dist_tt(self)


        def scatter_pl(self):
            plt.subplots(figsize=(5, 5))
            sns.scatterplot(df['age'], color='red')
            plt.legend('Age on Heart Disease')
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\scatter_pl.PNG')
            plt.show()

        scatter_pl(self)

        def scatter_se(self):
            plt.subplots(figsize=(5, 5))
            sns.scatterplot(df['sex'],color='red')
            plt.legend('Sex on Heart Disease')
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\scatter_se.PNG')
            plt.show()
        scatter_se(self)

        def scatter_cp(self):
            plt.subplots(figsize=(5, 5))
            sns.scatterplot(df['cp'],color='red')
            plt.legend('cp on Heart Disease')
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\scatter_cp.PNG')
            plt.show()
        scatter_cp(self)


        def scatter_tr(self):
            plt.subplots(figsize=(5, 5))
            sns.scatterplot(df['trestbps'],color='red')
            plt.legend('trestbps on Heart Disease')
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\scatter_tr.PNG')
            plt.show()
        scatter_tr(self)

        def scatter_ch(self):
            plt.subplots(figsize=(5, 5))
            sns.scatterplot(df['chol'],color='red')
            plt.legend('chol on Heart Disease')
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\scatter_ch.PNG')
            plt.show()
        scatter_ch(self)

        def scatter_fb(self):
            plt.subplots(figsize=(5, 5))
            sns.scatterplot(df['fbs'],color='red')
            plt.legend('fbs on Heart Disease')
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\scatter_fb.PNG')
            plt.show()
        scatter_fb(self)


        def scatter_re(self):
            plt.subplots(figsize=(5, 5))
            sns.scatterplot(df['restecg'],color='red')
            plt.legend('restecg on Heart Disease')
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\scatter_re.PNG')
            plt.show()
        scatter_re(self)



        def scatter_th(self):
            plt.subplots(figsize=(5, 5))
            sns.scatterplot(df['thalach'],color='red')
            plt.legend('thalach on Heart Disease')
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\scatter_th.PNG')
            plt.show()
        scatter_th(self)



        def scatter_ex(self):
            plt.subplots(figsize=(5, 5))
            sns.scatterplot(df['exang'],color='red')
            plt.legend('exang on Heart Disease')
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\scatter_ex.PNG')
            plt.show()
        scatter_ex(self)



        def scatter_ol(self):
            plt.subplots(figsize=(5, 5))
            sns.scatterplot(df['oldpeak'],color='red')
            plt.legend('oldpeak on Heart Disease')
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\scatter_ol.PNG')
            plt.show()
        scatter_ol(self)



        def scatter_sl(self):
            plt.subplots(figsize=(5, 5))
            sns.scatterplot(df['slope'],color='red')
            plt.legend('slope on Heart Disease')
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\scatter_sl.PNG')
            plt.show()
        scatter_sl(self)



        def scatter_ca(self):
            plt.subplots(figsize=(5, 5))
            sns.scatterplot(df['ca'],color='red')
            plt.legend('ca on Heart Disease')
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\scatter_ca.PNG')
            plt.show()
        scatter_ca(self)


        def scatter_tl(self):
            plt.subplots(figsize=(5, 5))
            sns.scatterplot(df['thal'],color='red')
            plt.legend('thal on Heart Disease')
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\scatter_tl.PNG')
            plt.show()
        scatter_tl(self)


        def scatter_tt(self):
            plt.subplots(figsize=(5, 5))
            sns.scatterplot(df['target'],color='red')
            plt.legend('target on Heart Disease')
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\scatter_tt.PNG')
            plt.show()
        scatter_tt(self)



        def age(self):
            plt.subplots(figsize=(5, 5))
            plt.title('Boxplot for Age')
            sns.boxplot(data=df['age'])
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\cage.PNG')
            plt.show()

        age(self)

        def sex(self):
            plt.subplots(figsize=(5, 5))
            plt.title('Boxplot for sex')
            sns.boxplot(data=df['sex'])
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\sex.PNG')
            plt.show()

        sex(self)

        def cp(self):
            plt.subplots(figsize=(5, 5))
            plt.title('Boxplot for cp')
            sns.boxplot(data=df['cp'])
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\cp.PNG')
            plt.show()

        cp(self)

        def trestbps(self):
            plt.subplots(figsize=(5, 5))
            plt.title('Boxplot for trestbps')
            sns.boxplot(data=df['trestbps'])
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\ct-bps.PNG')
            plt.show()

        trestbps(self)

        def chol(self):
            plt.subplots(figsize=(5, 5))
            plt.title('Boxplot for chol')
            sns.boxplot(data=df['chol'])
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\col.PNG')
            plt.show()

        chol(self)

        def fbs(self):
            plt.subplots(figsize=(5, 5))
            plt.title('Boxplot for fbs')
            sns.boxplot(data=df['fbs'])
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\heart_fbs.PNG')
            plt.show()

        fbs(self)

        def restecg(self):
            plt.subplots(figsize=(5, 5))
            plt.title('Boxplot for restecg')
            sns.boxplot(data=df['restecg'])
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\heart_ecg.PNG')
            plt.show()

        restecg(self)

        def thalach(self):
            plt.subplots(figsize=(5, 5))
            plt.title('Boxplot for thalach')
            sns.boxplot(data=df['thalach'])
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\ch.PNG')
            plt.show()

        thalach(self)

        def exang(self):
            plt.subplots(figsize=(5, 5))
            plt.title('Boxplot for exang')
            sns.boxplot(data=df['exang'])
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\ex.PNG')
            plt.show()

        exang(self)

        def oldpeak(self):
            plt.subplots(figsize=(5, 5))
            plt.title('Boxplot for oldpeak')
            sns.boxplot(data=df['oldpeak'])
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\old-peak.PNG')
            plt.show()

        oldpeak(self)

        def slope(self):
            plt.subplots(figsize=(5, 5))
            plt.title('Boxplot for slope')
            sns.boxplot(data=df['slope'])
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\heart_slope.PNG')
            plt.show()

        slope(self)

        def ca(self):
            plt.subplots(figsize=(5, 5))
            plt.title('Boxplot for ca')
            sns.boxplot(data=df['ca'])
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\heart_ca.PNG')
            plt.show()

        ca(self)

        def thal(self):
            plt.subplots(figsize=(5, 5))
            plt.title('Boxplot for thal')
            sns.boxplot(data=df['thal'])
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\heart_th.PNG')
            plt.show()

        thal(self)

        def target(self):
            plt.subplots(figsize=(5, 5))
            plt.title('Boxplot for target')
            sns.boxplot(data=df['target'])
            plt.savefig('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Visualization\heart_target.PNG')
            plt.show()

        target(self)

    except:
        print('Please check the code once again')


plots('dist_pl', 'dist_se', 'dist_cp', 'dist_tr', 'dist_ch', 'dist_fb', 'dist_re', 'dist_th', 'dist_ex', 'dist_ol', 'dist_sl', 'dist_ca', 'dist_tl', 'dist_tt', 'scatter_pl', 'scatter_se', 'scatter_cp', 'scatter_tr', 'scatter_ch', 'scatter_fb', 'scatter_re', 'scatter_th', 'scatter_ex', 'scatter_ol', 'scatter_sl', 'scatter_ca', 'scatter_tl', 'scatter_tt', 'bar_cha', 'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target')