
(cl:in-package :asdf)

(defsystem "trackbotCeral-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "trackbotMotors" :depends-on ("_package_trackbotMotors"))
    (:file "_package_trackbotMotors" :depends-on ("_package"))
  ))