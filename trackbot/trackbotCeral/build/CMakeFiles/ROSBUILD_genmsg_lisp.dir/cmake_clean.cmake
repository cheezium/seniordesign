FILE(REMOVE_RECURSE
  "../msg_gen"
  "../msg_gen"
  "../src/trackbotCeral/msg"
  "CMakeFiles/ROSBUILD_genmsg_lisp"
  "../msg_gen/lisp/trackbotMotors.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_trackbotMotors.lisp"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_lisp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
