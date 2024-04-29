<script setup>
</script>

<template>
    <div class="container">
      <div id="homepg_div">      
        <div id="homepg_picdiv">          
        </div>
        <div id="homepg_btndiv">
          <div id="homepg_btnheader">
            <img alt="Camera Icon" id="homepg_btnheaderpic" src="@/assets/Dcamera_icon.png"/>
            <h3>Photogram</h3>              
          </div>
          <div id="homepg_btncontent">
            <h5 class="text-center">
              Inspiring wanderlust and fostering a global community. 
            </h5>
            <p>               
              Explore geo-tagged photos from around the world, connect with fellow travelers, 
              and share adventures. Let others see the world through your lens! Whether you're a globetrotter or an armchair traveler, 
              Photogram invites you to capture the globe, one frame at a time.
              Connect with the community today!
            </p>
            <div id="homepg_btns">
              <button @click="$router.push('register')" type="button" id="homepg_btn1" class="btn"> Register</button>  
              <button @click="$router.push('login')" type="button" id="homepg_btn2" class="btn"> Login</button>
            </div>     
          </div>  
        </div>
      </div>
    </div>
</template>

<style>
  body{
    background-image: url('@/assets/greenwave.png');
    /*<a href="http://www.freepik.com">Designed by Kotkoa / Freepik</a> */
    background-size: 50%;
  }

  #homepg_div{
      display: grid;
      gap: 0px 10px;
      grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); 
      padding: 35px 20px 20px 20px;
  }

  #homepg_picdiv{
      border: 0.4px solid rgb(109, 109, 109);
      box-shadow: rgba(17, 17, 26, 0.1) 0px 0px 16px;
      border-radius: 2px 2px 2px 2px;
      background: url('@/assets/nature2_pic.jpg') no-repeat;
      background-size: cover;
  }

  #homepg_pic{
      width: 100%;
      min-height: 430px;
      max-height: 110%;
      object-fit: cover;
      border-radius: 1px 1px 1px 1px;
  }

  #homepg_btndiv{
      margin: 0, 0, 0, 20px;
      border: 0.1px solid #cfcfcf;
      box-shadow: rgba(0, 0, 0, 0.12) 0px 1px 3px, rgba(0, 0, 0, 0.24) 0px 1px 2px;
      border-radius: 3px 3px 3px 3px;
      padding: 40px 25px 25px 25px;
      background: rgba(255, 255, 255, 0.817);
  }

  #homepg_btnheader{
    display: flex;
    justify-content: center;
  }

  #homepg_btnheaderpic{
    margin: 0px 9px 15px 0px;
    width: 35px;
    height: 38px;
  }

  #homepg_btncontent p {
    padding: 0px 0px 20px 0px;
    text-align: center;
  }

  #homepg_btncontent h5 {
    padding: 0px 20px 0px 20px;
  }

  #homepg_btns{    
    display: flex;
    justify-content: center;
    margin: 20px 0px 10px 0px;
  }

  #homepg_btn1{
    background-color: #3E905C;
    color: #fff;
    margin: 20px 0px 0px 0px;
    width: 100%;
  }

  #homepg_btn1:hover {
    background-color: #347d5c;
    cursor: pointer;
  }

  #homepg_btn2{
    background-color: #493E90;
    color: #fff;
    margin: 20px 0px 0px 15px;
    width: 100%;
  }

  #homepg_btn2:hover {
    background-color: #472c6e;
    cursor: pointer;
  }
</style>