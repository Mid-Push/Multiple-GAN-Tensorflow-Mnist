import os
import sys
import scipy.misc
import numpy as np
from vanilla_gan import Vanilla_GAN
from dcgan import DCGAN
from cgan import CGAN
from infogan import InfoGAN
from wgan import WGAN
import tensorflow as tf

if __name__ == '__main__':
	model_name = sys.argv[1]
	dataset = sys.argv[2]
	with tf.Session() as sess:
		if model_name == 'cgan':
			model = CGAN(sess, dataset)
		elif model_name == 'vanilla_gan':
			model = Vanilla_GAN(sess, dataset)
		elif model_name == 'dcgan':
			model = DCGAN(sess, dataset)
		elif model_name == 'infogan':
			model = InfoGAN(sess, dataset)
		elif model_name == 'wgan':
			model = WGAN(sess, dataset)
		else:
			print("We cannot find this model")

		model.train()

		print("finish to train dcgan")
