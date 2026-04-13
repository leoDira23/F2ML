
import { useState } from "react";

export function useNotification(){

   const[texto, setTexto]= useState(null);
     function show(text){
        setTexto (text);
     }
     function hide(){
        setTexto (null)
     }
     return{texto, show, hide};
}

