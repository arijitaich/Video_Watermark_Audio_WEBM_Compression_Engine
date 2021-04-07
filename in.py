from pyffmpeg import FFmpeg

inp = 'in/f.mp4'
out = 'out/f.webm'

ff = FFmpeg()
ff.options("-i " + inp + " -i logo.png -filter_complex overlay=1500:1000 libvpx -crf 10 -b:v 1M -c:a libvorbis " + out +"")
output_file = ff.convert(inp, out)

print(output_file)




