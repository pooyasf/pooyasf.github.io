
function setup() {

   var canvas = createCanvas(500, 150);
   // Move the canvas so it’s inside our <div id="sketch-holder">.
   canvas.parent('sketch-holder');

   x = 0;
  background(255);
  noStroke();
  frameRate(30);
  h_array = [0,height*1/4,height*2/4,height*3/4];
  w_array = [0,width*1/6,width*2/6,width*3/6,width*4/6,width*5/6];

  mmbr_list = [];
  for(let i=0;i<24;i++){
    grp = floor(random(6));
    mmbr_list.push(grp);
  }
  t = 0;
}

function draw() {
    
    background(255);
    stroke(255);
    
    let grp_num = 0;
    for(let h_elmnt = 0;h_elmnt<4;h_elmnt++){
        for(let w_elmnt=0;w_elmnt<6;w_elmnt++){
            
            grp_clr_seed = mmbr_list[grp_num];

            fill(100+grp_clr_seed*30,150+sin(t/20)*10,150+grp_clr_seed+cos(t/50)*20);
            std_rect(w_array[w_elmnt],h_array[h_elmnt]);
            grp_num++;

        }
    }

    t++;


}

function std_rect(x,y){
    rect(x,y,width*1/6,height*1/4);
}