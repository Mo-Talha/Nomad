define([], function(){
   return {

       getOverflowedText: function(text, limit){
           var newText = text;

           for (var i = 0; i < text.length; i++){
               if (i > limit){
                   newText = newText.substring(0, i) + '..';
                   break;
               }
           }

           return newText;
       }

   };
});