<script setup>
    const props = defineProps(['movie']);
</script>

<template>
    <div class="post">
        <div id="postinfo">
            <div id="posterdiv">
                <img :src="movie.poster" class="poster" alt="...">
            </div>
            <h5 class="movietitle">{{ movie.title }}</h5>                    
            <p class="moviedesc">{{ movie.description }}</p>
        </div>     
    </div>
</template>
  
<style>
    /* Add any component specific styles here */
    .poster {
        width: 220px;
        height: 310px;
        object-fit: cover;
        border-radius: 6px 0px 0px 6px;
    }

    #posterdiv {
        float: left;
        margin: 0;
        padding-right: 15px;
    }

    .movie {    
        background: white;
        border: 0.5px solid #b9babb;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        border-radius: 6px 6px 6px 6px;
        min-height: 310px;
        position: relative;
    }

    #movieinfo {
        padding-right: 14.5px;
    }

    .movietitle {
        padding-top: 20px;
        color: rgb(49, 48, 48);
        font-weight: bold;
    }
    
    .moviedesc{
        padding-top: 10px;
        font-size: 15px;
    }

</style>