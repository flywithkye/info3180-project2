<script setup>
</script>

<template>    
    <main class="container py-5">
        <h1>Explore</h1>
        <div id="posts">
            <PostCard :post="post" v-for="post in posts" :key="post.id" />
        </div>
    </main>
</template>
  
<style>
    /* Add any component specific styles here */
    #posts {
        display: grid;
        gap: 30px 30px;
        grid-template-columns: minmax(0, 1fr);  
        padding: 15px 0px 15px 0px;
    }

</style>