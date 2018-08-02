<!doctype html>
<html class="no-js" lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>联系我们</title>
    <link rel="stylesheet" href="css/foundation.css">
    <link rel="stylesheet" href="css/app.css">
  </head>
  <body>
    <div class="grid-container">

      <!-- Top Bar Assembly -->
      <div class="small-12"  style="z-index: 666;"data-sticky-container id="DOOM">
        <!-- Used Z-index to place top-bar at top, always. 
        666 is just the largest number in use. 
        Needed in order to actually have the dropdown behave correctly. 

        Also, the top bar only works in big enough windows. Not sure how big is
        "big enough," but half the window doesn't work on my laptop.-->
        <div class="top-bar sticky" style="z-index: 666;"data-sticky data-margin-top="0">

          <div class="top-bar-left">
            <h4>龙磐投资</h4>
          </div>

          <div class="top-bar-right">
            <ul class="menu dropdown align-right" data-dropdown-menu>
              <li><a href="mainpage.html">首页</a></li>
              <li><a href="#">关于我们</a>

                <ul class="menu">
                  <li><a href="overview.html">公司概况</a></li>
                  <li><a href="team.html">团队</a></li>
                  <li><a href="casestudy.html">案例</a></li>
                  <li><a href="vc-funds.html">基金</a></li>
                </ul>

              </li>
              <li><a href="news.html">新闻</a></li>
              <li><a href="contactus.html" class="button">联系我们</a></li>
            </ul>
          </div>
          
        </div>
      </div>
      <!-- End Top Bar Assembly -->

      <div class="grid-x grid-padding-x">
        <div class="large-8 medium-8 cell sections">
          <!-- Example name and data card -->
          <div class="grid-x grid-padding-x">
            <div class="cell">
              <h2>相关新闻</h2>
              <p>(可以考虑在这里放一些内容)</p>
              <hr/>
            </div>
          </div>
        </div>

        <div class="large-4 medium-4 cell sticky-container" data-sticky-container style="z-index: 665;">
          <!-- <div 
            class="sticky callout" 
            data-sticky data-anchor="exampleId" 
            data-sticky-on="large" 
            data-stick-to="DOOM"
            >

            <h4>公司团队</h4>

            <ul class="vertical menu" data-magellan>
              <li><a href="#eins">余治华</a></li>
              <li><a href="#zwei">徐光宇</a></li>
              <li><a href="#drei">张发明</a></li>
              <li><a href="#vier">韩永信</a></li>
              <li><a href="#funf">孙慧</a></li>
              <li><a href="#sechs">李军红</a></li>
              <li><a href="#sieben">黄文娜</a></li>
              <li><a href="#acht">夏益</a></li>
            </ul>
          </div> -->
        </div> <!-- closes right side -->
      </div> <!-- closes non-topbar stuff -->
    </div> <!-- closes main container -->

    <script src="js/vendor/jquery.js"></script>
    <script src="js/vendor/what-input.js"></script>
    <script src="js/vendor/foundation.js"></script>
    <script src="js/app.js"></script>
  </body>
</html>
