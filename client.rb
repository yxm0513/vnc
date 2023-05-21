require 'net/vnc'

Net::VNC.open '10.151.116.163:1', :shared => true, :password => '' do |vnc|
  width = vnc.instance_variable_get("@framebuffer_width")
  length = vnc.instance_variable_get("@framebuffer_height")
  puts width
  puts length
  vnc.pointer_move 300 * width / 600, 315 * length / 1024 # 中文
  vnc.button_press
  sleep 1
  vnc.pointer_move 270 * width / 600, 885 * length / 1024 #网络
  vnc.button_press
  vnc.take_screenshot('screen1.png')
end
