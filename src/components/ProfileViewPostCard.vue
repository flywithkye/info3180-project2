<script setup>
    const props = defineProps(['post']);    
</script>

<template>
    <div class="post">
        <div id="postphotodiv">
            <img id="postphoto" :src="'../uploads/' + post.photo" alt="Post photo">
        </div>      
    </div>
</template>
  
<style scoped>
    /* Add any component specific styles here */
    .post {    
        background: white;
        border: 0.5px solid #b9babb;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        border-radius: 6px 6px 6px 6px;
        position: relative;
        /*margin-left: 50px;*/
    }

    #postphotodiv {
        margin: 0;
    }

    #postphoto {
        height: 35vh;
        width: 100%;
        object-fit: cover;
    }

</style>