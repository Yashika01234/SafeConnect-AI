
const trains=[

{

name:"Rajdhani Express",

price:2

},

{

name:"Vande Bharat",

price:2.5

},

{

name:"Shatabdi",

price:1.8

}

];



const distances={

"Delhi-Mumbai":1400,

"Delhi-Lucknow":550,

"Delhi-Jaipur":300,

"Mumbai-Lucknow":1350,

"Mumbai-Jaipur":1150,

"Lucknow-Jaipur":600

};



function searchTrain(){


let user=

document.getElementById(

"user"

).value;


let source=

document.getElementById(

"source"

).value;


let destination=

document.getElementById(

"destination"

).value;


let passengers=

Number(

document.getElementById(

"passengers"

).value

);



if(source==destination){

alert(

"Invalid Route"

);

return;

}


let key=

source+"-"+destination;


let reverse=

destination+"-"+source;


let distance=

distances[key]

||

distances[reverse]

||

800;


let html="";


trains.forEach(t=>{


let total=

Math.floor(

distance*

t.price*

passengers

);


html+=`

<div class="trainCard">


<h2>

${t.name}

</h2>


<p>

Distance:

${distance} KM

</p>


<p>

Passengers:

${passengers}

</p>


<p>

Price:

₹${total}

</p>


<button

onclick="bookTrain(

'${t.name}',

${total},

'${user}'

)">

Book Ticket

</button>


</div>

`;

});


document.getElementById(

"trains"

).innerHTML=

html;


}



function bookTrain(

name,

price,

user

){


let pnr=

Math.floor(

100000+

Math.random()

*900000

);


alert(

`

BOOKED SUCCESSFULLY

Train:

${name}

Passenger:

${user}

PNR:

${pnr}

Price:

₹${price}

`

);


localStorage.setItem(

pnr,

name

);


}