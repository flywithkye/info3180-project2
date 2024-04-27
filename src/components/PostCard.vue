<script setup>
    const props = defineProps(['post']);
</script>

<template>
    <div class="post">
        <div id="userdiv">
            <div id="userdivinner1">
                <img id="userphoto" alt="..." src="@/assets/nature_pic.jpg">
                <!-- meant to be like this: <img :src="post.profilepic" class="photo" alt="..."> -->

                <p>useruname</p>
                <!-- meant to be like this: <p>{{ post.username }}</p> -->
            </div>
                
            <div id="userdivinner2">
                <p id="postdate">April 29, 2024</p>
                <!-- meant to be like this: <p id="postdate">{{ post.date }}</p> -->
            </div>
        </div>

        <div id="postinfo">
            <div id="postphotodiv">
                <img id="postphoto" alt="..." src="@/assets/nature_pic.jpg">
                <!-- meant to be like this: <img id="postphoto" :src="post.photo" alt="..."> -->
            </div>
            <p id="postcaption"> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do 
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
                quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis 
                aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
                pariatur.
            </p>   
            <!-- meant to be like this: <p class="postcaption">{{ post.caption }}</p>  -->

            <div id="postdetails">
                <div id="postlikesdiv">
                    <img alt="Likes Icon" id="postlikesicon" src="@/assets/likes_icon.png"/>
                    <p id="postlikes"> Likes</p>
                    <!-- meant to be like this: <p id="postlikes">{{ post.likes }} Likes</p> -->
                </div>
                
                <div id="postsharediv">
                    <img alt="Share Icon" id="postshareicon" src="@/assets/share_icon.png"/>
                    <p id="postlikes">Share</p>
                </div>
            </div>                            
            
        </div>     
    </div>
</template>
  
<style>
    /* Add any component specific styles here */
    .post {    
        background: white;
        border: 0.5px solid #b9babb;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        border-radius: 6px 6px 6px 6px;
        max-width: 60vw;
        position: relative;
        /*margin-left: 50px;*/
    }

    #userdiv{
        display: flex;    
        justify-content: space-between;
        padding: 15px 20px 13px 15px;
        color: #3f3e3e;
    }

    #userdivinner1{
        display: flex;
    }
    
    #userphoto {
        width: 25px;
        height: 25px;
        object-fit: cover;
        border-radius: 50px;
        margin: 0px 10px 0px 0px;
    }

    #postinfo {
        margin-top: -15px;
    }

    #postphotodiv {
        margin: 0;
    }

    #postphotodivinner {
        margin: 0;
    }

    #postphoto {
        width: 100%;
        height: 330px;
        object-fit: cover;
    }

    #postcaption{
        padding: 10px 12px 10px 12px;
    }

    #postdetails{    
        display: flex;    
        justify-content: space-between;
        padding: 10px 20px 10px 20px;
        color: #3f3e3e;
    }

    #postlikesdiv{
        display: flex;
    }

    #postlikesicon{        
        margin: 0px 9px 15px 0px;
        width: 25px;
        height: 25px;
    }

    #postsharediv{
        display: flex;
    }

    #postshareicon{        
        margin: 0px 9px 15px 0px;
        width: 25px;
        height: 25px;
    }


</style>