## Lab Notebook
*--6.44.17--*

- **Descriptive statistics**, source of variation for parallel plates deflection (e.g. the explained variation in the linear regression model). Should be applied to the bounce experiements as well, cen use maximum -likelyhood parameter estimation from the model, or use the parameter optimization scheme. Chi-squared statistic to compare measured pdf from the sampled data to the theoretical density function.
- **Data Structures** Create HDF5 files from the particle tracking output csv's with *pytables* and tag them with experiemental metadata.
- Create functions for rest of analysis workflow (instead of one-off scripts).

*--8.02.17*

- Multiple bounces in a drop, but the smoothing works best on a series of individual bounces. I need to localte the bounce, partition the trajectories, and plot the acclerations vs. positions for each bounce series in a drop.
	- I can get the contact time for at least the first bounce by finding the first minima and maxima of the graph of circularity (or AR) vs time. I should compare this to the model of *Richards (2002)*. The airborn time is the time before and after 1 *T_j* about the minima of the droplet position.
	- I can already see, by this method at least, that the contact time is not symmetric about the bounce.
	- After the first bounce it's more difficult to see a pattern, the impacts occur at lower Weber numbers...
	- Make a function to the class that adds a new data attribute for individual bounces by slicing the 'drop.data' array on the bounds identifies by the position minima and the contact time.
	- Add an 'number of bounces' attribute to the drop object.
	- I can also get the contact time by subtracting the time from the 
- Still need to 'zero' the positions somehow:
	- I could use the YM position of the first frame (including the frames removed prior to filtering) as the zero, but I may have already added some bias when doing the video reduction.
	- I can use the position of the first impact (corrected for circularity and starting from the bottom, rather than the centroid of the drop), but some drops have no bounces also there may be some bias added by uncorrected movement of the camera.
- Still need to experiement a bit more witht the interpolation scheme in the S-G filter.
- Some of the data got inverted somehow on drop07131.
- Add univariate regression plot to the parallel plates analysis.
- Should I keep the double drop data?
	- Only of qualitative interest. The field model is clearly broken for this case.
- From now on keep the thesolded image series for each drop, for future reference.