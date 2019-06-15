require 'fileutils'

train_data_path = "./data/train/data.txt"
test_data_path = "./data/test/data.txt"

FileUtils.touch(train_data_path) unless FileTest.exist?(train_data_path)
FileUtils.touch(test_data_path) unless FileTest.exist?(test_data_path)


test_kim_data_paths = Dir.glob("./data/test/kim/*.jpg")
train_kim_data_paths = Dir.glob("./data/train/kim/*.jpg")


File.open(test_data_path, "w") do |f|
  test_kim_data_paths.each { |path| f.puts("#{path} 0") }
end
File.open(train_data_path, "w") do |f|
  train_kim_data_paths.each { |path| f.puts("#{path} 0") }
end
