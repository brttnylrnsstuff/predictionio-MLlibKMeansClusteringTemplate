


<!DOCTYPE html>
<html lang="en" class="">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Language" content="en">
    
    
    <title>predictionio-MLlibKMeansClusteringTemplate/README.md at master · sahiliitm/predictionio-MLlibKMeansClusteringTemplate</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png">
    <meta property="fb:app_id" content="1401488693436528">

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="sahiliitm/predictionio-MLlibKMeansClusteringTemplate" name="twitter:title" /><meta content="predictionio-MLlibKMeansClusteringTemplate - PredictionIO vanilla engine template (Scala-based parallelized engine) " name="twitter:description" /><meta content="https://avatars0.githubusercontent.com/u/5723372?v=3&amp;s=400" name="twitter:image:src" />
      <meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://avatars0.githubusercontent.com/u/5723372?v=3&amp;s=400" property="og:image" /><meta content="sahiliitm/predictionio-MLlibKMeansClusteringTemplate" property="og:title" /><meta content="https://github.com/sahiliitm/predictionio-MLlibKMeansClusteringTemplate" property="og:url" /><meta content="predictionio-MLlibKMeansClusteringTemplate - PredictionIO vanilla engine template (Scala-based parallelized engine) " property="og:description" />
      <meta name="browser-stats-url" content="/_stats">
    <link rel="assets" href="https://assets-cdn.github.com/">
    <link rel="conduit-xhr" href="https://ghconduit.com:25035">
    <link rel="xhr-socket" href="/_sockets">
    <meta name="pjax-timeout" content="1000">
    <link rel="sudo-modal" href="/sessions/sudo_modal">

    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="selected-link" value="repo_source" data-pjax-transient>
      <meta name="google-analytics" content="UA-3769691-2">

    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="CBC7D503:0964:2946779:55082972" name="octolytics-dimension-request_id" /><meta content="5723372" name="octolytics-actor-id" /><meta content="sahiliitm" name="octolytics-actor-login" /><meta content="ec6198f2c54234266652a95576fc9a30570a4846515a51ba10076278d1d24576" name="octolytics-actor-hash" />
    
    <meta content="Rails, view, blob#show" name="analytics-event" />

    
    <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">


    <meta content="authenticity_token" name="csrf-param" />
<meta content="a79uczBfB3Lc3Y9VS4AbJqU5cC+avQ722OqQKQ/2EzRZUl5zaQgGhfxM8Qzg/IY0s4ceQuqzHq9KafII1WFMZw==" name="csrf-token" />

    <link href="https://assets-cdn.github.com/assets/github-bb40a9aebece4c9c4c663b86dcbdfa070b4fb344f46e953335ac78df8770e3de.css" media="all" rel="stylesheet" />
    <link href="https://assets-cdn.github.com/assets/github2-58a463b2bc974b96204515f0ee8119f425ef37ad82a71625ed391d994c8d92a5.css" media="all" rel="stylesheet" />
    
    


    <meta http-equiv="x-pjax-version" content="468afcfdb5498790724eb756256558e2">

      
  <meta name="description" content="predictionio-MLlibKMeansClusteringTemplate - PredictionIO vanilla engine template (Scala-based parallelized engine) ">
  <meta name="go-import" content="github.com/sahiliitm/predictionio-MLlibKMeansClusteringTemplate git https://github.com/sahiliitm/predictionio-MLlibKMeansClusteringTemplate.git">

  <meta content="5723372" name="octolytics-dimension-user_id" /><meta content="sahiliitm" name="octolytics-dimension-user_login" /><meta content="30299501" name="octolytics-dimension-repository_id" /><meta content="sahiliitm/predictionio-MLlibKMeansClusteringTemplate" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="true" name="octolytics-dimension-repository_is_fork" /><meta content="29922117" name="octolytics-dimension-repository_parent_id" /><meta content="PredictionIO/template-scala-parallel-vanilla" name="octolytics-dimension-repository_parent_nwo" /><meta content="29922117" name="octolytics-dimension-repository_network_root_id" /><meta content="PredictionIO/template-scala-parallel-vanilla" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/sahiliitm/predictionio-MLlibKMeansClusteringTemplate/commits/master.atom" rel="alternate" title="Recent Commits to predictionio-MLlibKMeansClusteringTemplate:master" type="application/atom+xml">

  </head>


  <body class="logged_in  env-production linux vis-public fork page-blob">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div class="wrapper">
      
      
      


        <div class="header header-logged-in true" role="banner">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" data-ga-click="Header, go to dashboard, icon:logo">
  <span class="mega-octicon octicon-mark-github"></span>
</a>


      <div class="site-search repo-scope js-site-search" role="search">
          <form accept-charset="UTF-8" action="/sahiliitm/predictionio-MLlibKMeansClusteringTemplate/search" class="js-site-search-form" data-global-search-url="/search" data-repo-search-url="/sahiliitm/predictionio-MLlibKMeansClusteringTemplate/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
  <input type="text"
    class="js-site-search-field is-clearable"
    data-hotkey="s"
    name="q"
    placeholder="Search"
    data-global-scope-placeholder="Search GitHub"
    data-repo-scope-placeholder="Search"
    tabindex="1"
    autocapitalize="off">
  <div class="scope-badge">This repository</div>
</form>
      </div>
      <ul class="header-nav left" role="navigation">
        <li class="header-nav-item explore">
          <a class="header-nav-link" href="/explore" data-ga-click="Header, go to explore, text:explore">Explore</a>
        </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="https://gist.github.com" data-ga-click="Header, go to gist, text:gist">Gist</a>
          </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="/blog" data-ga-click="Header, go to blog, text:blog">Blog</a>
          </li>
        <li class="header-nav-item">
          <a class="header-nav-link" href="https://help.github.com" data-ga-click="Header, go to help, text:help">Help</a>
        </li>
      </ul>

    
<ul class="header-nav user-nav right" id="user-links">
  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link name" href="/sahiliitm" data-ga-click="Header, go to profile, text:username">
      <img alt="sahiliitm" class="avatar" data-user="5723372" height="20" src="https://avatars2.githubusercontent.com/u/5723372?v=3&amp;s=40" width="20" />
      <span class="css-truncate">
        <span class="css-truncate-target">sahiliitm</span>
      </span>
    </a>
  </li>

  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link js-menu-target tooltipped tooltipped-s" href="#" aria-label="Create new..." data-ga-click="Header, create new, icon:add">
      <span class="octicon octicon-plus"></span>
      <span class="dropdown-caret"></span>
    </a>

    <div class="dropdown-menu-content js-menu-content">
      
<ul class="dropdown-menu">
  <li>
    <a href="/new" data-ga-click="Header, create new repository, icon:repo"><span class="octicon octicon-repo"></span> New repository</a>
  </li>
  <li>
    <a href="/organizations/new" data-ga-click="Header, create new organization, icon:organization"><span class="octicon octicon-organization"></span> New organization</a>
  </li>


    <li class="dropdown-divider"></li>
    <li class="dropdown-header">
      <span title="sahiliitm/predictionio-MLlibKMeansClusteringTemplate">This repository</span>
    </li>
      <li>
        <a href="/sahiliitm/predictionio-MLlibKMeansClusteringTemplate/settings/collaboration" data-ga-click="Header, create new collaborator, icon:person"><span class="octicon octicon-person"></span> New collaborator</a>
      </li>
</ul>

    </div>
  </li>

  <li class="header-nav-item">
        <a href="/notifications" aria-label="You have no unread notifications" class="header-nav-link notification-indicator tooltipped tooltipped-s" data-ga-click="Header, go to notifications, icon:read" data-hotkey="g n">
        <span class="mail-status all-read"></span>
        <span class="octicon octicon-inbox"></span>
</a>
  </li>

  <li class="header-nav-item">
    <a class="header-nav-link tooltipped tooltipped-s" href="/settings/profile" id="account_settings" aria-label="Settings" data-ga-click="Header, go to settings, icon:settings">
      <span class="octicon octicon-gear"></span>
    </a>
  </li>

  <li class="header-nav-item">
    <form accept-charset="UTF-8" action="/logout" class="logout-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="kR1WMeHaglT9csjw2EgzPbNdpG+zGVGghYii8An92Orib5LAb4kKnldnavWEz87db24XQAXsWP16fG0YrTiRYw==" /></div>
      <button class="header-nav-link sign-out-button tooltipped tooltipped-s" aria-label="Sign out" data-ga-click="Header, sign out, icon:logout">
        <span class="octicon octicon-sign-out"></span>
      </button>
</form>  </li>

</ul>


    
  </div>
</div>

        

        


      <div id="start-of-content" class="accessibility-aid"></div>
          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    <div id="js-flash-container">
      
    </div>
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        
<ul class="pagehead-actions">

  <li>
      <form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="wRtwFlu964dE++pvVIup6xyKY+r0iKXD+L9IlaWTYx2xMC22+c45PzlPpukpUpb6sVftqzaMiaV2L6ZJetkiLw==" /></div>    <input id="repository_id" name="repository_id" type="hidden" value="30299501" />

      <div class="select-menu js-menu-container js-select-menu">
        <a href="/sahiliitm/predictionio-MLlibKMeansClusteringTemplate/subscription"
          class="minibutton select-menu-button with-count js-menu-target" role="button" tabindex="0" aria-haspopup="true"
          data-ga-click="Repository, click Watch settings, action:blob#show">
          <span class="js-select-button">
            <span class="octicon octicon-eye"></span>
            Unwatch
          </span>
        </a>
        <a class="social-count js-social-count" href="/sahiliitm/predictionio-MLlibKMeansClusteringTemplate/watchers">
          1
        </a>
        
        <div class="select-menu-modal-holder">
          <div class="select-menu-modal subscription-menu-modal js-menu-content" aria-hidden="true">
            <div class="select-menu-header">
              <span class="select-menu-title">Notifications</span>
              <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
            </div>

            <div class="select-menu-list js-navigation-container" role="menu">

              <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                <span class="select-menu-item-icon octicon octicon-check"></span>
                <div class="select-menu-item-text">
                  <input id="do_included" name="do" type="radio" value="included" />
                  <span class="select-menu-item-heading">Not watching</span>
                  <span class="description">Be notified when participating or @mentioned.</span>
                  <span class="js-select-button-text hidden-select-button-text">
                    <span class="octicon octicon-eye"></span>
                    Watch
                  </span>
                </div>
              </div>

              <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
                <span class="select-menu-item-icon octicon octicon octicon-check"></span>
                <div class="select-menu-item-text">
                  <input checked="checked" id="do_subscribed" name="do" type="radio" value="subscribed" />
                  <span class="select-menu-item-heading">Watching</span>
                  <span class="description">Be notified of all conversations.</span>
                  <span class="js-select-button-text hidden-select-button-text">
                    <span class="octicon octicon-eye"></span>
                    Unwatch
                  </span>
                </div>
              </div>

              <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                <span class="select-menu-item-icon octicon octicon-check"></span>
                <div class="select-menu-item-text">
                  <input id="do_ignore" name="do" type="radio" value="ignore" />
                  <span class="select-menu-item-heading">Ignoring</span>
                  <span class="description">Never be notified.</span>
                  <span class="js-select-button-text hidden-select-button-text">
                    <span class="octicon octicon-mute"></span>
                    Stop ignoring
                  </span>
                </div>
              </div>

            </div>

          </div>
        </div>
      </div>
</form>
  </li>

  <li>
    
  <div class="js-toggler-container js-social-container starring-container ">

    <form accept-charset="UTF-8" action="/sahiliitm/predictionio-MLlibKMeansClusteringTemplate/unstar" class="js-toggler-form starred js-unstar-button" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="RzSa/S/utz2RG7heiKYGVtkrZN5AzSRsv0I69MGEW5CCc2HTA7/wpVrpFP67GbH4J8y5edYPDn+nn9OI70Je3Q==" /></div>
      <button
        class="minibutton with-count js-toggler-target"
        aria-label="Unstar this repository" title="Unstar sahiliitm/predictionio-MLlibKMeansClusteringTemplate"
        data-ga-click="Repository, click unstar button, action:blob#show; text:Unstar">
        <span class="octicon octicon-star"></span>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/sahiliitm/predictionio-MLlibKMeansClusteringTemplate/stargazers">
          0
        </a>
</form>
    <form accept-charset="UTF-8" action="/sahiliitm/predictionio-MLlibKMeansClusteringTemplate/star" class="js-toggler-form unstarred js-star-button" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="yWcGLYyKYBSV5x7liJkvVGDh9lnwAGBqSCKWz7+BvvxxMM7JbORWg8C062j6DnHEtEmx5lWLJoo0wwq7+Ti+mQ==" /></div>
      <button
        class="minibutton with-count js-toggler-target"
        aria-label="Star this repository" title="Star sahiliitm/predictionio-MLlibKMeansClusteringTemplate"
        data-ga-click="Repository, click star button, action:blob#show; text:Star">
        <span class="octicon octicon-star"></span>
        Star
      </button>
        <a class="social-count js-social-count" href="/sahiliitm/predictionio-MLlibKMeansClusteringTemplate/stargazers">
          0
        </a>
</form>  </div>

  </li>

        <li>
          <form accept-charset="UTF-8" action="/sahiliitm/predictionio-MLlibKMeansClusteringTemplate/fork" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="tu5AiF+JKhaeO3oyHawRj45vbuhtmnTBObcLyrvFktJ0H5+rCWIDTtQkijrHZME4CdSfw0j7vzKBwlaleU0deQ==" /></div>
            <button
                type="submit"
                class="minibutton with-count"
                data-ga-click="Repository, show fork modal, action:blob#show; text:Fork"
                title="Fork your own copy of sahiliitm/predictionio-MLlibKMeansClusteringTemplate to your account"
                aria-label="Fork your own copy of sahiliitm/predictionio-MLlibKMeansClusteringTemplate to your account">
              <span class="octicon octicon-repo-forked"></span>
              Fork
            </button>
            <a href="/sahiliitm/predictionio-MLlibKMeansClusteringTemplate/network" class="social-count">8</a>
</form>        </li>

</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="mega-octicon octicon-repo-forked"></span>
          <span class="author"><a href="/sahiliitm" class="url fn" itemprop="url" rel="author"><span itemprop="title">sahiliitm</span></a></span><!--
       --><span class="path-divider">/</span><!--
       --><strong><a href="/sahiliitm/predictionio-MLlibKMeansClusteringTemplate" class="js-current-repository" data-pjax="#js-repo-pjax-container">predictionio-MLlibKMeansClusteringTemplate</a></strong>

          <span class="page-context-loader">
            <img alt="" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
          </span>

            <span class="fork-flag">
              <span class="text">forked from <a href="/PredictionIO/template-scala-parallel-vanilla">PredictionIO/template-scala-parallel-vanilla</a></span>
            </span>
        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      <div class="repository-with-sidebar repo-container new-discussion-timeline  ">
        <div class="repository-sidebar clearfix">
            
<nav class="sunken-menu repo-nav js-repo-nav js-sidenav-container-pjax js-octicon-loaders"
     role="navigation"
     data-pjax="#js-repo-pjax-container"
     data-issue-count-url="/sahiliitm/predictionio-MLlibKMeansClusteringTemplate/issues/counts">
  <ul class="sunken-menu-group">
    <li class="tooltipped tooltipped-w" aria-label="Code">
      <a href="/sahiliitm/predictionio-MLlibKMeansClusteringTemplate" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /sahiliitm/predictionio-MLlibKMeansClusteringTemplate">
        <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>


    <li class="tooltipped tooltipped-w" aria-label="Pull requests">
      <a href="/sahiliitm/predictionio-MLlibKMeansClusteringTemplate/pulls" aria-label="Pull requests" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g p" data-selected-links="repo_pulls /sahiliitm/predictionio-MLlibKMeansClusteringTemplate/pulls">
          <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull requests</span>
          <span class="js-pull-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>


      <li class="tooltipped tooltipped-w" aria-label="Wiki">
        <a href="/sahiliitm/predictionio-MLlibKMeansClusteringTemplate/wiki" aria-label="Wiki" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g w" data-selected-links="repo_wiki /sahiliitm/predictionio-MLlibKMeansClusteringTemplate/wiki">
          <span class="octicon octicon-book"></span> <span class="full-word">Wiki</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>      </li>
  </ul>
  <div class="sunken-menu-separator"></div>
  <ul class="sunken-menu-group">

    <li class="tooltipped tooltipped-w" aria-label="Pulse">
      <a href="/sahiliitm/predictionio-MLlibKMeansClusteringTemplate/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-selected-links="pulse /sahiliitm/predictionio-MLlibKMeansClusteringTemplate/pulse">
        <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>

    <li class="tooltipped tooltipped-w" aria-label="Graphs">
      <a href="/sahiliitm/predictionio-MLlibKMeansClusteringTemplate/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-selected-links="repo_graphs repo_contributors /sahiliitm/predictionio-MLlibKMeansClusteringTemplate/graphs">
        <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>
  </ul>


    <div class="sunken-menu-separator"></div>
    <ul class="sunken-menu-group">
      <li class="tooltipped tooltipped-w" aria-label="Settings">
        <a href="/sahiliitm/predictionio-MLlibKMeansClusteringTemplate/settings" aria-label="Settings" class="js-selected-navigation-item sunken-menu-item" data-selected-links="repo_settings /sahiliitm/predictionio-MLlibKMeansClusteringTemplate/settings">
          <span class="octicon octicon-tools"></span> <span class="full-word">Settings</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>      </li>
    </ul>
</nav>

              <div class="only-with-full-nav">
                  
<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone">
  <h3><span class="text-emphasized">HTTPS</span> clone URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="https://github.com/sahiliitm/predictionio-MLlibKMeansClusteringTemplate.git" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="clone-url "
  data-protocol-type="ssh"
  data-url="/users/set_protocol?protocol_selector=ssh&amp;protocol_type=clone">
  <h3><span class="text-emphasized">SSH</span> clone URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="git@github.com:sahiliitm/predictionio-MLlibKMeansClusteringTemplate.git" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone">
  <h3><span class="text-emphasized">Subversion</span> checkout URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="https://github.com/sahiliitm/predictionio-MLlibKMeansClusteringTemplate" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>



<p class="clone-options">You can clone with
  <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>, <a href="#" class="js-clone-selector" data-protocol="ssh">SSH</a>, or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <a href="https://help.github.com/articles/which-remote-url-should-i-use" class="help tooltipped tooltipped-n" aria-label="Get help on which URL is right for you.">
    <span class="octicon octicon-question"></span>
  </a>
</p>



                <a href="/sahiliitm/predictionio-MLlibKMeansClusteringTemplate/archive/master.zip"
                   class="minibutton sidebar-button"
                   aria-label="Download the contents of sahiliitm/predictionio-MLlibKMeansClusteringTemplate as a zip file"
                   title="Download the contents of sahiliitm/predictionio-MLlibKMeansClusteringTemplate as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
              </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          

<a href="/sahiliitm/predictionio-MLlibKMeansClusteringTemplate/blob/a79f27febd9d9e0c852b1576c84209e286aced78/README.md" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:cd58861dc947d876f5b60d890ee4f216 -->

<div class="file-navigation js-zeroclipboard-container">
  
<div class="select-menu js-menu-container js-select-menu left">
  <span class="minibutton select-menu-button js-menu-target css-truncate" data-hotkey="w"
    data-master-branch="master"
    data-ref="master"
    title="master"
    role="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Find or create a branch…" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Find or create a branch…">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Find or create a branch…" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/sahiliitm/predictionio-MLlibKMeansClusteringTemplate/blob/master/README.md"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="master">
                master
              </span>
            </a>
        </div>

          <form accept-charset="UTF-8" action="/sahiliitm/predictionio-MLlibKMeansClusteringTemplate/branches" class="js-create-branch select-menu-item select-menu-new-item-form js-navigation-item js-new-item-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="xOMI71xjpnosoCmmwqTM4omIcj70j6wv5G6HFb/wDMCgU21yMKpvzxpKBpTUmjCt0PBCzti1yZG/08Bwt5BCfA==" /></div>
            <span class="octicon octicon-git-branch select-menu-item-icon"></span>
            <div class="select-menu-item-text">
              <span class="select-menu-item-heading">Create branch: <span class="js-new-item-name"></span></span>
              <span class="description">from ‘master’</span>
            </div>
            <input type="hidden" name="name" id="name" class="js-new-item-value">
            <input type="hidden" name="branch" id="branch" value="master">
            <input type="hidden" name="path" id="path" value="README.md">
</form>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/sahiliitm/predictionio-MLlibKMeansClusteringTemplate/tree/v0.1.0/README.md"
                 data-name="v0.1.0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="v0.1.0">v0.1.0</a>
            </div>
        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

  <div class="button-group right">
    <a href="/sahiliitm/predictionio-MLlibKMeansClusteringTemplate/find/master"
          class="js-show-file-finder minibutton empty-icon tooltipped tooltipped-s"
          data-pjax
          data-hotkey="t"
          aria-label="Quickly jump between files">
      <span class="octicon octicon-list-unordered"></span>
    </a>
    <button aria-label="Copy file path to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
  </div>

  <div class="breadcrumb js-zeroclipboard-target">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/sahiliitm/predictionio-MLlibKMeansClusteringTemplate" class="" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">predictionio-MLlibKMeansClusteringTemplate</span></a></span></span><span class="separator">/</span><strong class="final-path">README.md</strong>
  </div>
</div>


  <div class="commit file-history-tease">
    <div class="file-history-tease-header">
        <img alt="sahiliitm" class="avatar" data-user="5723372" height="24" src="https://avatars0.githubusercontent.com/u/5723372?v=3&amp;s=48" width="24" />
        <span class="author"><a href="/sahiliitm" rel="author">sahiliitm</a></span>
        <time datetime="2015-03-17T13:13:59Z" is="relative-time">Mar 17, 2015</time>
        <div class="commit-title">
            <a href="/sahiliitm/predictionio-MLlibKMeansClusteringTemplate/commit/a79f27febd9d9e0c852b1576c84209e286aced78" class="message" data-pjax="true" title="Update README.md">Update README.md</a>
        </div>
    </div>

    <div class="participation">
      <p class="quickstat">
        <a href="#blob_contributors_box" rel="facebox">
          <strong>1</strong>
           contributor
        </a>
      </p>
      
    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
          <li class="facebox-user-list-item">
            <img alt="sahiliitm" data-user="5723372" height="24" src="https://avatars0.githubusercontent.com/u/5723372?v=3&amp;s=48" width="24" />
            <a href="/sahiliitm">sahiliitm</a>
          </li>
      </ul>
    </div>
  </div>

<div class="file">
  <div class="file-header">
    <div class="file-actions">
      <div class="button-group">
        <a href="/sahiliitm/predictionio-MLlibKMeansClusteringTemplate/raw/master/README.md" class="minibutton " id="raw-url">Raw</a>
          <a href="/sahiliitm/predictionio-MLlibKMeansClusteringTemplate/blame/master/README.md" class="minibutton js-update-url-with-hash">Blame</a>
        <a href="/sahiliitm/predictionio-MLlibKMeansClusteringTemplate/commits/master/README.md" class="minibutton " rel="nofollow">History</a>
      </div><!-- /.button-group -->


            <form accept-charset="UTF-8" action="/sahiliitm/predictionio-MLlibKMeansClusteringTemplate/edit/master/README.md" aria-label="Edit this file" class="tooltipped tooltipped-e inline-form edit-file-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="U0+6M0HvLr+fX5Nls3B2sx85NC3k8EIsVYfyOuFAAUNfC37Dgnz8SPOguaDdXqpFnu2fYveZCxNoB/LDMZRocw==" /></div>
              <button class="web-edit-button"
                      type="submit"
                      data-hotkey="e"
                      data-disable-with>
                <span class="octicon octicon-pencil"></span>
              </button>
</form>
          <form accept-charset="UTF-8" action="/sahiliitm/predictionio-MLlibKMeansClusteringTemplate/delete/master/README.md" aria-label="Delete this file" class="tooltipped tooltipped-s inline-form delete-file-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="yye3wRzlPLXfcYJsIRifdW5Vdzj41ruTiPkNuvbkw8HezTfwDqT1Wvo0os2akuNhfDEsVYrWGFeioPKIeSh6Eg==" /></div>
            <button class="web-edit-button"
                    type="submit"
                    data-disable-with>
              <span class="octicon octicon-trashcan "></span>
            </button>
</form>      </a>
    </div><!-- /.actions -->
    <div class="file-info">
        149 lines (91 sloc)
        <span class="file-info-divider"></span>
      6.149 kb
    </div>
  </div>
    <div id="readme" class="blob instapaper_body">
    <article class="markdown-body entry-content" itemprop="mainContentOfPage"><h1>
<a id="user-content-predictionio-mllibkmeansclusteringtemplate" class="anchor" href="#predictionio-mllibkmeansclusteringtemplate" aria-hidden="true"><span class="octicon octicon-link"></span></a>predictionio-MLlibKMeansClusteringTemplate</h1>

<p>PredictionIO clustering engine template (Scala-based parallelized engine) </p>

<h2>
<a id="user-content-overview" class="anchor" href="#overview" aria-hidden="true"><span class="octicon octicon-link"></span></a>Overview</h2>

<p>This is an application which demonstrates the use of K-Means clustering algorithm which can be deployed on
a spark-cluster using prediction.io. Let's go over the whole procedure to get the app running step-wise. Note
that it's assumed that the python SDK for prediction io has been installed and works seemlessly with 
python2.7. It has also been assumed that the preiction.io binaries have been added to PATH environment
variable. If it hasn't been it can be done by editing '~/.bashrc'</p>

<h2>
<a id="user-content-clustering" class="anchor" href="#clustering" aria-hidden="true"><span class="octicon octicon-link"></span></a>Clustering</h2>

<p><a href="https://camo.githubusercontent.com/d472d46f6fdcf69666e7b02f37b388d1c60a995a/687474703a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f7468756d622f342f34362f4c696e6561722d73766d2d73636174746572706c6f742e7376672f37323070782d4c696e6561722d73766d2d73636174746572706c6f742e7376672e706e67" target="_blank"><img src="https://camo.githubusercontent.com/d472d46f6fdcf69666e7b02f37b388d1c60a995a/687474703a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f7468756d622f342f34362f4c696e6561722d73766d2d73636174746572706c6f742e7376672f37323070782d4c696e6561722d73766d2d73636174746572706c6f742e7376672e706e67" alt="Text" data-canonical-src="http://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Linear-svm-scatterplot.svg/720px-Linear-svm-scatterplot.svg.png" style="max-width:100%;"></a></p>

<p>Cluster analysis or clustering is the task of grouping a set of objects in such a way that objects in the same group (called a cluster) are more similar (in some sense or another) to each other than to those in other groups (clusters). It is a main task of exploratory data mining, and a common technique for statistical data analysis, used in many fields, including machine learning, pattern recognition, image analysis, information retrieval, and bioinformatics.</p>

<p>In centroid-based clustering (the kind we use in this template), clusters are represented by a central vector, which may not necessarily be a member of the data set. When the number of clusters is fixed to k, k-means clustering gives a formal definition as an optimization problem: find the k cluster centers and assign the objects to the nearest cluster center, such that the squared distances from the cluster are minimized.</p>

<h2>
<a id="user-content-training-data" class="anchor" href="#training-data" aria-hidden="true"><span class="octicon octicon-link"></span></a>Training Data</h2>

<p>The training data used is a set of public data sets that can be found at </p>

<pre><code>http://cs.joensuu.fi/sipu/datasets/
</code></pre>

<p>The data set used in the default implementation of this template is <em>jain.txt</em>.</p>

<h2>
<a id="user-content-building-the-app-with-preidictionio" class="anchor" href="#building-the-app-with-preidictionio" aria-hidden="true"><span class="octicon octicon-link"></span></a>Building the App with Preidiction.io</h2>

<p>First, some pre-conditions which must be met.</p>

<p>1)  The directory where this code is to reside must have write permissions. This can be tested by 
    executing a 'mkdir a' command. If the permissions do not exist they can be granted by executing:</p>

<pre><code>    sudo chmod -R 777  .
</code></pre>

<p>2)  Prediction.io must be installed. The most recommended way to get prediction.io is to clone the 
    repository and build from source. It also has several dependencies which can be looked up here:
      <a href="http://docs.prediction.io/install/">http://docs.prediction.io/install/</a></p>

<p>Actual installation procedure(Linux-type Systems):</p>

<p>3)  Clone the current repository by executing the following command in the directory where you want 
    the code to reside:</p>

<pre><code>  git clone https://github.com/sahiliitm/predictionio-MLlibKMeansClusteringTemplate.git
</code></pre>

<p>4)  We need a corresponding app with which the engine has to communicate. Create a new app using the commandand        also note down the details regarding the app in a text file called say 'info.txt'. These will be 
    required for the engine and app to communicate: </p>

<pre><code>  pio app new MyApp
</code></pre>

<p>5)  Mofidy 'engine.json' to reflect the AppID of the app you just created. By default it has the id of the app
    which I last created.</p>

<p>6)  We're now good to go and can put all the pieces together and make sure that the engine and app talk together.
    Towards that end, start HBase by executing 'start-hbase.sh'. The following command does so:</p>

<pre><code>  ./HBASE_HOME/bin/start-hbase.sh
</code></pre>

<p>7)  Start elastic search.</p>

<pre><code>  ./ELASTIC_SEARCH_HOME/bin/elasticsearch
</code></pre>

<p>8)  Check that both the components are working well by running:</p>

<pre><code>  pio status
</code></pre>

<p>9)  Having confirmed that all components work well, run the eventserver which will capture all the relevant
    events and which the Engine would later query to build it's model.</p>

<pre><code>  pio eventserver
</code></pre>

<p>10) Modify the python script 'submitData.py' to reflect the appID of your app which you had saved in 
    'info.txt'. Execute it to convey the various points to be clustered by the K-Means algorithm as follows:</p>

<pre><code>  python2.7 submitData.py
</code></pre>

<p>11) Run the following in the directory where the code resides to build the model: </p>

<pre><code>  pio build
</code></pre>

<p>12) Run the following to train the model:</p>

<pre><code>  pio train
</code></pre>

<p>13) Run the following to deploy the model:</p>

<pre><code>  pio deploy
</code></pre>

<p>14) Having deployed the engine, we can check that it's up and running using a standard web browser at the URL</p>

<pre><code>  http://localhost:8000
</code></pre>

<p>15) Finally, we can run a python script such as 'getPredictions.py' to get predictions for new data-Points.
    Run:</p>

<pre><code>  python2.7 getPredictions.py
</code></pre>

<h2>
<a id="user-content-usage-of-the-engine" class="anchor" href="#usage-of-the-engine" aria-hidden="true"><span class="octicon octicon-link"></span></a>Usage of the Engine</h2>

<h3>
<a id="user-content-input-for-training" class="anchor" href="#input-for-training" aria-hidden="true"><span class="octicon octicon-link"></span></a>Input For training:</h3>

<p>Any input to the Engine for the sake of training is a data point and has the following fields:</p>

<ol class="task-list">
<li>entity_type : This is always set to 'point' in this case since there is just a single type of entity which this engine works with a data point.</li>
<li>entity_id : This is the unique id which each data point has, and which the engine can use internally to                        distinguish various data points.</li>
<li>
<p>properties  : The attributes of the data point. Can include the true label too, to evaluate the clustering     algorithm being used. The example included includes:</p>

<p>"attr0" : First attribute,</p>

<p>"attr1" : Second attribute,</p>

<p>"plan"  : The true label for the data point</p>
</li>
</ol>

<p>A sample query looks as follows(Using Python SDK):</p>

<div class="highlight highlight-python"><pre>client.create_event(
<span class="pl-vpf">event</span><span class="pl-k">=</span><span class="pl-s1"><span class="pl-pds">"</span>$set<span class="pl-pds">"</span></span>,
<span class="pl-vpf">entity_type</span><span class="pl-k">=</span><span class="pl-s1"><span class="pl-pds">"</span>point<span class="pl-pds">"</span></span>,
<span class="pl-vpf">entity_id</span><span class="pl-k">=</span>i,
<span class="pl-vpf">properties</span><span class="pl-k">=</span> {
        <span class="pl-s1"><span class="pl-pds">"</span>attr0<span class="pl-pds">"</span></span> : <span class="pl-c1">12.6</span>,
        <span class="pl-s1"><span class="pl-pds">"</span>attr1<span class="pl-pds">"</span></span> : <span class="pl-c1">1.5</span>,
        <span class="pl-s1"><span class="pl-pds">"</span>plan<span class="pl-pds">"</span></span> : <span class="pl-c1">1</span>
        }
    )</pre></div>

<h3>
<a id="user-content-input-for-prediction" class="anchor" href="#input-for-prediction" aria-hidden="true"><span class="octicon octicon-link"></span></a>Input for Prediction</h3>

<p>The input query is a simple JSON object with field <strong>dataPoint</strong>. A typical query looks as follows whem using Python SDK:</p>

<div class="highlight highlight-python"><pre>engine_client.send_query({<span class="pl-s1"><span class="pl-pds">"</span>dataPoint<span class="pl-pds">"</span></span>: [<span class="pl-c1">12.1</span>, <span class="pl-c1">15.1</span>]})</pre></div>

<p>This returns a PredictedResult object described in next section.</p>

<h3>
<a id="user-content-output" class="anchor" href="#output" aria-hidden="true"><span class="octicon octicon-link"></span></a>Output</h3>

<p>It is an object of class <strong>PredictedResult</strong> and has a single field, the predicted label, of type Double.
It is returned as a JSON object by the engine and looks like this:</p>

<div class="highlight highlight-javascript"><pre>{u<span class="pl-s1"><span class="pl-pds">'</span>cluster<span class="pl-pds">'</span></span><span class="pl-k">:</span> <span class="pl-c1">0.0</span>}</pre></div>
</article>
  </div>

</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links right">
        <li><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
      <li><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>

    </ul>

    <a href="https://github.com" aria-label="Homepage">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
</a>
    <ul class="site-footer-links">
      <li>&copy; 2015 <span title="0.04863s from github-fe142-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact</a></li>
    </ul>
  </div>
</div>


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-suggester-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="fullscreen-contents js-fullscreen-contents" placeholder=""></textarea>
      <div class="suggester-container">
        <div class="suggester fullscreen-suggester js-suggester js-navigation-container"></div>
      </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped tooltipped-w" aria-label="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped tooltipped-w"
      aria-label="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    
    

    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-x flash-close js-ajax-error-dismiss" aria-label="Dismiss error"></a>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-d2f4f76d6a05f07ed67ef9f94d3823b34f98232770518bc7f8f40de8846ec511.js"></script>
      <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-91ece02a84d5c082fd9e33151224c3da0d2604a68dade3703dfedf44d75decd4.js"></script>
      
      

  </body>
</html>

