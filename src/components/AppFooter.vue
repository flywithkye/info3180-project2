<template>
      <footer>
          <div id="footerdiv">
              <p id="footertxt">Copyright &copy {{ year }} Dayna Clare, Tareque Robinson, Sheamar White</p>
          </div>
      </footer>
</template>

<script setup>
import { ref } from "vue";

const year = (new Date).getFullYear();
</script>

<style>
/* Add any component specific styles here */
footer{
    left: 0;
    bottom: 0;    
    margin-bottom: 0px;
    margin-top: 40px;
    width: 100%;
}

#footerdiv{    
    background: rgba(255, 255, 255);  
    padding: 23px 0px 8px 0px;
    border-top: 1.5px solid rgb(179, 179, 179);
    border-bottom: 1.5px solid rgb(179, 179, 179);
}

#footertxt{
    margin-left: 80px;
    color: #333333;
}
</style>