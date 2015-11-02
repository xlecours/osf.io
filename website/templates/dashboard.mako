<%inherit file="base.mako"/>
<%def name="title()">Dashboard</%def>

<%def name="container_class()">container-xxl</%def>

<%def name="content()">
% if disk_saving_mode:
    <div class="alert alert-info"><strong>NOTICE: </strong>Forks, registrations, and uploads will be temporarily disabled while the OSF undergoes a hardware upgrade. These features will return shortly. Thank you for your patience.</div>
% endif

  <h3>Projects </h3>
  <p>Browse and organize all your projects</p>

  <div class="row">
    <div id="poFilter" class="col-xs-12 col-sm-10 col-sm-offset-1 col-md-8 col-md-offset-2 col-lg-6 col-lg-offset-3 m-t-sm m-b-sm"></div>
  </div>

  <div id="fileBrowser" class="fileBrowser" ></div>


%if 'badges' in addons_enabled:
    <div class="row">
        <div class="col-sm-5">
            <div class="page-header">
              <button class="btn btn-primary pull-right" id="newBadge" type="button">New Badge</button>
                <h3>Your Badges</h3>
            </div>
            <div mod-meta='{
                     "tpl": "../addons/badges/templates/dashboard_badges.mako",
                     "uri": "/api/v1/dashboard/get_badges/",
                     "replace": true
                }'></div>
        </div>
        <div class="col-sm-5">
            <div class="page-header">
                <h3>Badges You've Awarded</h3>
            </div>
        </div><!-- end col -->
    </div><!-- end row -->
%endif
</%def>

<%def name="stylesheets()">
    ${parent.stylesheets()}
    <link rel="stylesheet" href="/static/css/file-browser.css">
</%def>

<%def name="javascript_bottom()">
<script>
    window.contextVars = $.extend(true, {}, window.contextVars, {
        currentUser: {
            'id': '${user_id}'
        }
    });
</script>
<script src=${"/static/public/js/dashboard-page.js" | webpack_asset}></script>

</%def>
