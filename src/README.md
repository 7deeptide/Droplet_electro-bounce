## Partial to-do list for the Drop-Bounce parameter estimation
- [x] Find contact time with ellipse fit parameters.
   
   *Using the ellipse function contact is not very trustworthy on its own*. It might be interesting to try using a TV filter on the Circularity data, and adding some sort of decision critera to the mask creation. TV filtering should work better than Savitsky-Golay for piecewise continuous data. Also, from lit. review I expect the contact time to not be symmetrical about the minimimum centroid position, this might be born out by the Circularity data, but not by the ellipse function masking. *I need to review the actual drop videos.* This is a critical issue; I need to remove edge effect bias from the derivatives or they're useless. 
   
- [x] Check filtering `dt`.

   Resample with fft, or use a spline fit to make the data and time arrays the same length. This is important because the Savitsky-Golay filter doesn't allow non-constant `dt`.
   
- [x] Add partitioning based on contact time.

   Make (greater/less than) minm a boolean mask and `logical_and` add to the contact mask. This works in most cases, but in a few places (small bounces), the `argrelextrema` algorithem returns mins that break partitioning. I hope that this can be fixed with improved video, otherwise these drops should be excluded.
   
- [x] Add absolute criteria for YM zero.

   Still need a plan for non-bounce ref. points. Probably the best way to do this is with a fiduciary marking in frame as a "cannonical zero" reference.
   
- [x] Count number of partitions, add acceleration plots for each.

   Going to use a cheesey approach, `while: True try: n=n+1 except:ValueError break`. Also `IndexError` and `UnboundLocalError`. I can catch the IndexErrors by counting the number of bounces in the drop prior to the exception (if `0` then it's a no-bounce drop, and the next `n+1` should drop an `UnboundLocalError`). *Still need this for contact time tj, but for now I'm only going to use the first drop in parameter estimation*.
   
- [x] Finish functionalizing the munging.
- [x] Add analytical functions for Re, tj vs. We.
- [x] Check `savgol` docs for suitability of other interpolation modes.

- [x] Add numerical derivatives of del.E^2 for dielectrophoresis.
- [x] Extract simulation parameters from ODE solver and plot all simulation forces on same (log) axis.
- [x] Review parameter estimation - expected variance, maximum likelyhood.

   The most promising approach is to minimize the objective function (the SSE or Chi^2 between the model and data), using a Nelder-Mead optimizer. Use as many parameters as possible (lest risk making the problem ill-posed), but constrain them using an exterior penalty function. The parameters can be constrained from theory, or from the mean +/- 2 standard deviation of the measured values, or from the measurement precision where applicable. The parameters with the most uncertainty are the surface potential, and the droplet charge. It's possible that good correspondence is not possible between the model and the data. This is especially true for cases where there is significant lateral migration of the droplets durin the drop. In this case the primary assumption of electric field as a function of z-position only breaks down. We can see this in the acceleration plots (as a sideways 'u' shape). 
   
- [x] finish adding the exterior penalty function.

   The Nelder-Mead algorithem has very poor convergence when an exterior penalty function is used. Gradient based methods fail to minimize the objective function, and I cannot explicity compute the Hessian or Jacobians for the objective function. Sci-py does not allow me to impliment simple box constraints with Nelder-Mead. The chi-squared fucntion is somewhat noisey, but otherwise I'm not sure if the objective function is well posed (it is not an explicit function, because it is a comparison between noisey experiemental data and the solution to a non-linear ODE which is numerically integrated). The Chi-squared function seems to be overflowing very easily. The function call time could probably be dramatically improved.

- [x] add function to calculate sigma from surfaceV
- [ ] non-dimensionalize the ODE/determine the appropriate electric parameter
- [x] loop over all drops in the set and append the initial and final design vectors to a csv file
- [x] move the impact plots to the bottom, and color the lines by an electric parameter
- [ ] 'alldrops' trajectory plot colored by electric parameter
- [x] fix drop.surfaceV datatype
