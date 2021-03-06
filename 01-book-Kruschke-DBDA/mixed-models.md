## Mixed models in genetics

h2r

* [paper](https://www.researchgate.net/publication/236253076_Bayesian_inference_of_mixed_models_in_quantitative_genetics_of_crop_species) for pedigrees (sib-pairs) + JAGS code
          * Code in a better format from the thesis http://alexandria.cpd.ufv.br:8000/teses/genetica%20e%20melhoramento/2012/247890f.pdf
* JAGS applied to twin studies http://scheibehenne.de/Scheibehenne.et.al.Appetite2014.onlineSupplement.pdf
      * similar example https://www.utwente.nl/bms/omd/Medewerkers/vandenbergfiles/schwabevandenbergBG2013.pdf
* Animan model in Stan https://groups.google.com/forum/#!topic/stan-users/2eZ11QG_pbU


Fine mapping

* http://cc.oulu.fi/~misillan/Assoc_Map_WinBUGS_1.txt from http://cc.oulu.fi/~misillan/

## Mixed models

General notes

* By Ben Bolker: https://www.nceas.ucsb.edu/system/files/mixed.pdf

Scripts

* Correlation between RE https://github.com/mclark--/Miscellaneous-R-Code/blob/master/ModelFitting/Bayesian/rstan_MixedModelSleepstudy_withREcorrelation.R

Tutorials

* Fitting linear mixed models using JAGS and Stan: A tutorial http://www.ling.uni-potsdam.de/~vasishth/JAGSStanTutorial/SorensenVasishthMay12014.pdf
    * Model under study: `RTi = beta0 + beta1 * conditioni + ei`
* Workshop "Practical Data Analysis with JAGS using R": http://bendixcarstensen.com/Bayes/Cph-2012/pracs.pdf

Discussions 

* JAGS model for `lmer(y ~ a + x + a:x + (1 + a | id))`: http://stats.stackexchange.com/a/28655/8598

Blog posts

* glmer2stan: https://hlplab.wordpress.com/2013/12/13/going-full-bayesian-with-mixed-effects-regression-models/
* http://people.ucsc.edu/~abrsvn/general-random-effects-jags.html
      * Lecture: http://www.unc.edu/courses/2010fall/ecol/563/001/docs/lectures/lecture28.htm
