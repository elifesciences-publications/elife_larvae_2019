import matplotlib.pyplot as plt
import skimage.io
import numpy
data_path= '/Users/tim/Google Drive/2pdata/01_30_2016/'
im=skimage.io.imread(data_path + 'Streaming Phasor Capture - 5_XY0_Z0_T00_C0.tif')
im_mean=np.mean(im,axis=0)
#plt.colormap('hot')
plt.figure()
im_cut=im_mean[150:250,150:250]
plt.imshow(im_cut)
zoom_xlim=[150,230]
zoom_ylim=[250,140]

#plot scale bar
microns_per_pixel=1.47441
pixels_in_50_microns=50./microns_per_pixel
init_scale_height=80
init_scale_x=60

plt.plot([init_scale_x,init_scale_x+pixels_in_50_microns],[init_scale_height, init_scale_height])
zoom_xlim=[150,230]
zoom_ylim=[250,140]
from roipoly import RoiPoly

#choose roi
my_roi=RoiPoly(color='c')
my_roi.display_roi()

mask1=my_roi.get_mask(im_cut)
mask2=my_roi2.get_mask(im_cut)
im_cut_all=im[:,150:250,150:250]

###hack 
num_frames=len(im_cut_all[:,0,0])
mn_roi1=[]
mn_roi2=[]
for crframe in np.arange(num_frames):
	mn_roi1.append(np.mean(im_cut_all[crframe,mask1]))
	
	mn_roi2.append(np.mean(im_cut_all[crframe,mask2]))

###
#now plot the means
####
plt.figure()
tmlapse_in_s=.11963
xvls=np.arange(0,40*tmlapse_in_s,tmlapse_in_s)
plt.plot(xvls[0:9],mn_roi1[0:9],'c')
plt.plot(xvls[14:],mn_roi1[14:],'c')
plt.plot(xvls[0:9],mn_roi2[0:9],'g')
plt.plot(xvls[14:],mn_roi2[14:],'g')
plt.ylim([0,5000])
plt.xlim([0,5])


#Load GCAMP tif...
im_gcamp=skimage.io.imread(data_path+'A08aGCaMP_SuccessfulStim_AcquisitionPlane_XY0_Z0_T0_C0.tif')
im_chrimson=skimage.io.imread(data_path+'dbdChrimson_SuccessfulStim_StimPlane_XY0_Z0_T0_C0.tif')

#first plot average pixel intensity
zoom_xlim=[150,230]
zoom_ylim=[250,140]

###plot all frames as series of rows.
import matplotlib.gridspec as gridspec
fig = plt.figure()
num_rows=4
num_col=10
rowct=0
colct=0
gs = gridspec.GridSpec(num_rows, num_col, figure=fig)
tmlapse_in_s=.11963
for cr_frame in np.arange(40):
	#col_vl=np.mod(cr_frame,num_rows)
	print('colct=%d'%colct)
	#row_vl=np.mod(cr_frame,num_col)
	ax=fig.add_subplot(gs[rowct,colct])
	plt.imshow(im[cr_frame,:])
	plt.xlim(zoom_xlim)
	plt.ylim(zoom_ylim)
	ax.spines['right'].set_visible(False)
	ax.spines['top'].set_visible(False)
	ax.spines['bottom'].set_visible(False)
	ax.spines['left'].set_visible(False)
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)
	crtime=cr_frame*tmlapse_in_s
	title_text='%.2f'%crtime
	plt.title(title_text,fontsize=8)
	#ax.tick_params(bottom='off',left='off')

	if colct==num_col-1:
		rowct=rowct+1
		colct=0
	else:
		colct=colct+1



#then plot variance of pixel intensity