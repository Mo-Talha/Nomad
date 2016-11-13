define([], function(){
   return {

       getRandomColor: function(){
            return '#'+(Math.random()*0xFFFFFF<<0).toString(16);
       }

   };
});