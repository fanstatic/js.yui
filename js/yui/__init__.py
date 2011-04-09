from fanstatic import Library, Resource

# This code is auto-generated and not PEP8 compliant

yui = Library('yui', 'resources')

fonts = Resource(yui, 'fonts/fonts.css', minified='fonts/fonts-min.css')
grids = Resource(yui, 'grids/grids.css', depends=[fonts], minified='grids/grids-min.css')
yahoo = Resource(yui, 'yahoo/yahoo.js', debug='yahoo/yahoo-debug.js', minified='yahoo/yahoo-min.js')
dom = Resource(yui, 'dom/dom.js', depends=[yahoo], debug='dom/dom-debug.js', minified='dom/dom-min.js')
event = Resource(yui, 'event/event.js', depends=[yahoo], debug='event/event-debug.js', minified='event/event-min.js')
element = Resource(yui, 'element/element.js', depends=[dom, event], debug='element/element-debug.js', minified='element/element-min.js')
progressbar = Resource(yui, 'progressbar/progressbar.js', depends=[element], debug='progressbar/progressbar-debug.js', minified='progressbar/progressbar-min.js')
event_mouseenter = Resource(yui, 'event-mouseenter/event-mouseenter.js', depends=[dom, event], debug='event-mouseenter/event-mouseenter-debug.js', minified='event-mouseenter/event-mouseenter-min.js')
containercore = Resource(yui, 'container/container_core.js', depends=[dom, event], debug='container/container_core-debug.js', minified='container/container_core-min.js')
calendar = Resource(yui, 'calendar/calendar.js', depends=[event, dom], debug='calendar/calendar-debug.js', minified='calendar/calendar-min.js')
datemath = Resource(yui, 'datemath/datemath.js', depends=[yahoo], debug='datemath/datemath-debug.js', minified='datemath/datemath-min.js')
paginator = Resource(yui, 'paginator/paginator.js', depends=[element], debug='paginator/paginator-debug.js', minified='paginator/paginator-min.js')
container = Resource(yui, 'container/container.js', depends=[dom, event], debug='container/container-debug.js', minified='container/container-min.js')
simpleeditor = Resource(yui, 'editor/simpleeditor.js', depends=[element], debug='editor/simpleeditor-debug.js', minified='editor/simpleeditor-min.js')
menu = Resource(yui, 'menu/menu.js', depends=[containercore], debug='menu/menu-debug.js', minified='menu/menu-min.js')
event_simulate = Resource(yui, 'event-simulate/event-simulate.js', depends=[event], debug='event-simulate/event-simulate-debug.js', minified='event-simulate/event-simulate-min.js')
cookie = Resource(yui, 'cookie/cookie.js', depends=[yahoo], debug='cookie/cookie-debug.js', minified='cookie/cookie-min.js')
storage = Resource(yui, 'storage/storage.js', depends=[yahoo, event, cookie], debug='storage/storage-debug.js', minified='storage/storage-min.js')
json = Resource(yui, 'json/json.js', depends=[yahoo], debug='json/json-debug.js', minified='json/json-min.js')
swf = Resource(yui, 'swf/swf.js', depends=[element], debug='swf/swf-debug.js', minified='swf/swf-min.js')
datasource = Resource(yui, 'datasource/datasource.js', depends=[event], debug='datasource/datasource-debug.js', minified='datasource/datasource-min.js')
charts = Resource(yui, 'charts/charts.js', depends=[element, json, swf, datasource], debug='charts/charts-debug.js', minified='charts/charts-min.js')
yuiloader_dom_event = Resource(yui, 'yuiloader-dom-event/yuiloader-dom-event.js')
animation = Resource(yui, 'animation/animation.js', depends=[dom, event], debug='animation/animation-debug.js', minified='animation/animation-min.js')
button = Resource(yui, 'button/button.js', depends=[element], debug='button/button-debug.js', minified='button/button-min.js')
editor = Resource(yui, 'editor/editor.js', depends=[menu, element, button], debug='editor/editor-debug.js', minified='editor/editor-min.js')
carousel = Resource(yui, 'carousel/carousel.js', depends=[element], debug='carousel/carousel-debug.js', minified='carousel/carousel-min.js')
logger = Resource(yui, 'logger/logger.js', depends=[event, dom], debug='logger/logger-debug.js', minified='logger/logger-min.js')
dragdrop = Resource(yui, 'dragdrop/dragdrop.js', depends=[dom, event], debug='dragdrop/dragdrop-debug.js', minified='dragdrop/dragdrop-min.js')
reset_fonts_grids = Resource(yui, 'reset-fonts-grids/reset-fonts-grids.css')
slider = Resource(yui, 'slider/slider.js', depends=[dragdrop], debug='slider/slider-debug.js', minified='slider/slider-min.js')
colorpicker = Resource(yui, 'colorpicker/colorpicker.js', depends=[slider, element], debug='colorpicker/colorpicker-debug.js', minified='colorpicker/colorpicker-min.js')
resize = Resource(yui, 'resize/resize.js', depends=[dragdrop, element], debug='resize/resize-debug.js', minified='resize/resize-min.js')
imagecropper = Resource(yui, 'imagecropper/imagecropper.js', depends=[dragdrop, element, resize], debug='imagecropper/imagecropper-debug.js', minified='imagecropper/imagecropper-min.js')
get = Resource(yui, 'get/get.js', depends=[yahoo], debug='get/get-debug.js', minified='get/get-min.js')
event_delegate = Resource(yui, 'event-delegate/event-delegate.js', depends=[event], debug='event-delegate/event-delegate-debug.js', minified='event-delegate/event-delegate-min.js')
stylesheet = Resource(yui, 'stylesheet/stylesheet.js', depends=[yahoo], debug='stylesheet/stylesheet-debug.js', minified='stylesheet/stylesheet-min.js')
yuitest = Resource(yui, 'yuitest/yuitest.js', depends=[logger], debug='yuitest/yuitest-debug.js', minified='yuitest/yuitest-min.js')
element_delegate = Resource(yui, 'element-delegate/element-delegate.js', depends=[element], debug='element-delegate/element-delegate-debug.js', minified='element-delegate/element-delegate-min.js')
utilities = Resource(yui, 'utilities/utilities.js')
sam = Resource(yui, 'assets/skins/sam/skin.css')
reset = Resource(yui, 'reset/reset.css', minified='reset/reset-min.css')
base = Resource(yui, 'base/base.css', depends=[reset], minified='base/base-min.css')
uploader = Resource(yui, 'uploader/uploader.js', depends=[element], debug='uploader/uploader-debug.js', minified='uploader/uploader-min.js')
layout = Resource(yui, 'layout/layout.js', depends=[element], debug='layout/layout-debug.js', minified='layout/layout-min.js')
profiler = Resource(yui, 'profiler/profiler.js', depends=[yahoo], debug='profiler/profiler-debug.js', minified='profiler/profiler-min.js')
yuiloader = Resource(yui, 'yuiloader/yuiloader.js', debug='yuiloader/yuiloader-debug.js', minified='yuiloader/yuiloader-min.js')
profilerviewer = Resource(yui, 'profilerviewer/profilerviewer.js', depends=[profiler, yuiloader, element], debug='profilerviewer/profilerviewer-debug.js', minified='profilerviewer/profilerviewer-min.js')
datatable = Resource(yui, 'datatable/datatable.js', depends=[element, datasource], debug='datatable/datatable-debug.js', minified='datatable/datatable-min.js')
swfstore = Resource(yui, 'swfstore/swfstore.js', depends=[element, cookie, swf], debug='swfstore/swfstore-debug.js', minified='swfstore/swfstore-min.js')
selector = Resource(yui, 'selector/selector.js', depends=[yahoo, dom], debug='selector/selector-debug.js', minified='selector/selector-min.js')
connectioncore = Resource(yui, 'connection/connection_core.js', depends=[event], debug='connection/connection_core-debug.js', minified='connection/connection_core-min.js')
tabview = Resource(yui, 'tabview/tabview.js', depends=[element], debug='tabview/tabview-debug.js', minified='tabview/tabview-min.js')
reset_fonts = Resource(yui, 'reset-fonts/reset-fonts.css')
autocomplete = Resource(yui, 'autocomplete/autocomplete.js', depends=[dom, event, datasource], debug='autocomplete/autocomplete-debug.js', minified='autocomplete/autocomplete-min.js')
connection = Resource(yui, 'connection/connection.js', depends=[event], debug='connection/connection-debug.js', minified='connection/connection-min.js')
yahoo_dom_event = Resource(yui, 'yahoo-dom-event/yahoo-dom-event.js')
imageloader = Resource(yui, 'imageloader/imageloader.js', depends=[event, dom], debug='imageloader/imageloader-debug.js', minified='imageloader/imageloader-min.js')
swfdetect = Resource(yui, 'swfdetect/swfdetect.js', depends=[yahoo], debug='swfdetect/swfdetect-debug.js', minified='swfdetect/swfdetect-min.js')
treeview = Resource(yui, 'treeview/treeview.js', depends=[event, dom], debug='treeview/treeview-debug.js', minified='treeview/treeview-min.js')
history = Resource(yui, 'history/history.js', depends=[event], debug='history/history-debug.js', minified='history/history-min.js')