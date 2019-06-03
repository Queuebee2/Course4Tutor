// code hieronder gekopieerd van youtube filmpje
//https://www.youtube.com/watch?v=9rKuJrONnGQ


let canvas = document.querySelector('canvas');
canvas.width= 1000;
canvas.height=500;

let xGrid = 25;
let yGrid = 25;
let grootte_celen = 25;
let context = canvas.getContext('2d');

// Hier komt de dummy data, omdat ik iig nog geen gegevens heb
let data = {
    bacterie:55,
    schimmel: 64,
    overig: 40
};

const entries = Object.entries(data);

function drawGrids()
{
    context.beginPath();
    while(xGrid < canvas.height)
    {
      context.moveTo(0,xGrid);
      context.lineTo(canvas.width,xGrid);
      xGrid += grootte_celen;
    }

    while(yGrid < canvas.width)
    {
      context.moveTo(yGrid,0);
      context.lineTo(yGrid,canvas.height);
      yGrid += grootte_celen;
    }

    context.strokeStyle = "#69968C";
    context.stroke();
}

function blocks(count)
{
    return count * 25;
}

function drawAxis()
{
    let yPlot=18;
    let pop=0;
    context.beginPath();
    context.strokeStyle= "red";
    // verplaatst cursor naar 2e cel van xas en yas (als je van linksboven bekijkt)
    context.moveTo(blocks(2),blocks(2));
    // lijn begint op die 2e cel en gaat 18*25 naar beneden
    context.lineTo(blocks(2),blocks(18));
    // lijn begint op y(18) en gaat verder naar x(35)
    context.lineTo(blocks(35),blocks(18)); //travel 20 blocks to the right

    context.moveTo(blocks(18),blocks(2));
    for(let i=1; i<=10;i++)
    {
        context.strokeText(pop,blocks(1),blocks(yPlot));
        yPlot -= 2;
        pop += 2;
    }
    context.stroke();
}


function drawChart()
{
    context.beginPath();
    context.strokeStyle = "Blue";
    context.moveTo(blocks(2), blocks(18));

    var xPlot = 10;

    for(const [compost,population] of entries)
    {
        var populationInBlocks=population/5;
        context.lineTo(blocks(xPlot), blocks(18-populationInBlocks));
        xPlot += 5;

    }

    context.stroke();

}

drawGrids();
drawAxis();
drawChart();


