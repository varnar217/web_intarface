var myBarchart = new Barchart(
    {
        canvas:myCanvas,
        padding:10,
        gridScale:5,
        gridColor:"#eeeeee",
        data:myVinyls,
        colors:["#a55ca5","#67b6c7", "#bccd7a","#eb9743"]
    }
);
myBarchart.draw();