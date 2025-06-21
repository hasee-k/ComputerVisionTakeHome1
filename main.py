from intensity_reduction import reduce_intensity_levels 
from spatial_averaging import average_filter
from block_average import block_average 
from rotation import rotate_image




def main():
    
   
    path = 'image1.jpg'  
    
    ### Apply intensity reduction ###
    
      #Greyscale
    reduce_intensity_levels(path, 2, False)
    reduce_intensity_levels(path, 16, False) 
    
    # RGB
    reduce_intensity_levels(path, 2, True) 
    reduce_intensity_levels(path, 16, True)  
     
    
    ### Apply spatial averaging ###
    average_filter(path, 3, False) 
    average_filter(path, 10, False) 
    average_filter(path, 20, False) 
    # RGB
    average_filter(path, 3, True) 
    average_filter(path, 10, True) 
    average_filter(path, 20, True) 
    
    
    ### Apply rotation ###
    rotate_image(path, 45)  
    rotate_image(path, 90)  
    
    ## Apply block averaging ###
    
    #Greyscale
    block_average(path, 3, False)
    block_average(path, 5, False)      
    block_average(path, 7, False)
    # RGB 
    block_average(path, 3, True) 
    block_average(path, 5, True)
    block_average(path, 7, True)
    
    

    

if __name__ == "__main__":
    main()