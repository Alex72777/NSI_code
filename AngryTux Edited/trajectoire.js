function trajectoire(Vint,angle,t)
{
var g=9.81;
var x;
var y;
var h;
//h=0 pour Angry Tux
h=0;
x=Math.cos(angle)*Vint*t;
y=-1/2*g*(t*t)*+Math.sin(angle)*Vint*t+h;
return [x,y]
}

console.log(trajectoire(10,10,3))
