<script setup>
    import { ref, onMounted } from "vue"; 
    import PostCard from "@/components/PostCard.vue";

    let posts = ref([]); 

    onMounted(() => {
        fetchPosts();
    });

    function fetchPosts() {
        fetch("http://localhost:8080/api/v1/posts", { 
            method: 'GET',
        }) 
            .then(function (response) { 
                return response.json(); 
            }) 
            .then(function (data) { 
                posts.value = data.data;
                console.log(data); 
            }) 
            .catch(function (error) { 
                console.log(error); 
            });
    }
</script>

<template>    
    <main class="container">
        <div id="posts">
            <PostCard :post="post" v-for="post in posts" :key="post.id" />
        </div>
    </main>
</template>
  
<style scoped>
    /* Add any component specific styles here */
    #posts {
        display: grid;
        gap: 50px 30px;
        grid-template-columns: minmax(0, 1fr);  
        padding: 15px 0px 15px 0px;
    }

</style>