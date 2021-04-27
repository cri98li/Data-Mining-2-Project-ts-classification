import numpy as np

def Toy_Time_Series(ff, time, 
                    n_series_for_cluster = 10, 
                    n_cluster = 3,
                    random_state = None,
                    r_ampl = None,
                    r_off =  None,
                    iterargs = None, 
                    **kwargs
                    ):
    """
     --------------------------
    |
    | Author: Edoardo Gabrielli
    |
     --------------------------
    |
    | DESCRIPTION:
    | Function that build a toy model for a time series clustering problem.
    |
     --------------------------
    |
    | INPUT PARAMETERS:
    | - ff: func
    |   The function that rules the toy model. This function need one argument:
    |      1) x: numpy nd-array, shape: (n_series_for_cluster, time) 
    |         This represent the array that will be filled with the function (for one single cluster)
    |      Optional:
    |      2) **kwargs (anything you want) other parameters that you need for the model 
    |      Example: 
    |      def ff(x, q = 0, phi=0):
    |          return np.sin(x + phi) + q       
    |         
    | - time: numpy 1d array
    |   Time step in wich every series will be evaluated.
    |   
    | - n_series_for_cluster: int, default = 10
    |   Number of time series for clusters.
    |   
    | - n_cluster: int, default = 3
    |   Number of clusters.
    | 
    | - random_state: int, default = None
    |   Numpy seed for reproducibility. 
    |   If none it will not set the seed.
    |   
    | - r_ampl: int or float (positive), default = None
    |   Amplitude of random fluctuation on the function func.
    |   If None the random fluctiation is deactivated.
    |   
    | - r_off: int or float (positive), default = None
    |   Random offset on the y axis for the function func. Usefull to separate different time series of
    |   the same cluster.
    |   If None no offset will be applied to func.
    |   
    | - iterargs: list of dict of shape (n_cluster, ), default = None
    |   Iterable argument for the function ff (if you wanna pass different argument to different clusters).
    |   If None the algorithm do not pass anithing to the function here (but it will still pass **kwargs).
    |   
    | - **kwargs: 
    |   All the parameters that the function "ff" needs (in the previous example you need to pass phi here).
    | 
     ------------------------
    |
    | OTPUT PARAMETERS:
    | - yy: numpy nd-array of shape (n_cluster * n_series_for_cluster, len(time)) 
    |   Matrix with the data for the clustering task.
    |
     ------------------------    
    FULL EXAMPLES OF USAGE:
    1) Use of **kwargs
    >>> def func(x, q = 0, phi = 0):
    >>>     return np.sin(x + phi) + q
    >>> n = 100
    >>> xx = np.linspace(0, 2*np.pi, n)
    >>> yy = Time_Series_Cluster_Building(func, xx, q = 1, phi = 3)
    
    2) Use of iterargs and **kwargs with plot:
    >>> def func(x, q = 0, phi = 0):
    >>>     return np.sin(x + phi) + q
    >>> n = 100
    >>> iters = [dict(phi=2), dict(phi=3), dict(phi=4)]
    >>> xx = np.linspace(0, 2*np.pi, n)
    >>> yy = Time_Series_Cluster_Building(func, xx, q = 0, iterargs=iters)
    >>> plt.plot(yy.T)
    >>> plt.show()
    """
    # Some useful function...
    def add_noise(xx, r_ampl, r_off):
        """
        Evaluate noise for the group of curve of a single cluster.
        """
        if r_ampl != None:
            ampls = np.random.rand(*(xx.shape))*r_ampl # Random noise on amplitude
        else:
            ampls = np.zeros(xx.shape)
        if r_off != None:
            offs_num = (2*np.random.rand(xx.shape[0])-1)*r_off  # Random noise on y offset
            offs = np.broadcast_to(offs_num, xx.T.shape).T # Brodcasting to adjust dimention
        else:
            offs = np.zeros(xx.shape)
        return ampls + offs
    
    ############################################
    if random_state != None:
        np.random.seed(random_state)
        
    step = len(time)
    xx = np.full(shape = ( n_series_for_cluster * n_cluster, step ), # Build matrix of 
                 fill_value=time )                 # flat lines of the right shape

    yy = np.empty(xx.shape) # Empty array (this will contain the final time series)
    
    if iterargs==None:
        for i in range(n_cluster):
            lower_bond = i * n_series_for_cluster
            upper_bond = (i + 1) * n_series_for_cluster
            yy[lower_bond: upper_bond, :] = ff(xx[lower_bond: upper_bond, :], **kwargs)
            yy[lower_bond: upper_bond, :] += add_noise(xx[lower_bond: upper_bond, :], r_ampl, r_off)
    else: 
        for i, others in zip(range(n_cluster), iterargs):
            lower_bond = i * n_series_for_cluster
            upper_bond = (i + 1) * n_series_for_cluster
            yy[lower_bond: upper_bond, :] = ff(xx[lower_bond: upper_bond, :], **others, **kwargs)
            yy[lower_bond: upper_bond, :] += add_noise(xx[lower_bond: upper_bond, :], r_ampl, r_off)
    return yy