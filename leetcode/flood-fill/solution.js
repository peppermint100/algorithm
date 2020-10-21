var floodFill = function(image, sr, sc, newColor) {
    if(image[sr][sc] == newColor) return image
    const oldColor = image[sr][sc]
    
    fill(image, sr, sc, oldColor, newColor)

    return image
};

var fill = (image, sr, sc, oldColor, newColor) =>{
    if(!image) return
    if(sr < 0 || sc < 0 || sr >= image.length || sc >= image[0].length || image[sr][sc] != oldColor) return
   
    image[sr][sc] = newColor
    
    fill(image, sr + 1, sc, oldColor, newColor)
    fill(image, sr - 1, sc, oldColor, newColor)
    fill(image, sr, sc + 1, oldColor, newColor)
    fill(image, sr, sc - 1, oldColor, newColor)
}
