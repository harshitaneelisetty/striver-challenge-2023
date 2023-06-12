#https://www.codingninjas.com/codestudio/problems/flood-fill-algorithm_8230806?challengeSlug=striver-sde-challenge

def helper(image, i, j, old_color, new_color):
    if i < 0 or i >= len(image) or j < 0 or j >= len(image[0]):
        return

    if image[i][j] != old_color:
        return

    if image[i][j] == new_color:
        return

    image[i][j] = new_color

    helper(image, i, j + 1, old_color, new_color)
    helper(image, i, j - 1, old_color, new_color)
    helper(image, i + 1, j, old_color, new_color)
    helper(image, i - 1, j, old_color, new_color)

def floodFill(image, x, y, new_color):
    old_color = image[x][y]
    helper(image, x, y, old_color, new_color)
    return image
  
#i created helper function to recursively fill the neighboring pixels starting from the given coordinates (i, j) with a new color
#if they have the same color as the initial pixel
#in floodFill function i initialized the old color from the starting pixel
#i called the helper function to perform the flood fill operation

  
  
  
  
  
