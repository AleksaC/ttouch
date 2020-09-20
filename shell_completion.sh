_TTOUCH_TEMPLATE_DIR=${TTOUCH_TEMPLATE_DIR:-"$HOME/.templates"}

if [ -n "$ZSH_VERSION" ]; then
    function _ttouch(){
        compadd $(ls -A $_TTOUCH_TEMPLATE_DIR)
    }
    compdef _ttouch ttouch
elif [ -n "$BASH_VERSION" ]; then
    function _ttouch() {
        COMPREPLY=($(compgen -W "$(ls -A $_TTOUCH_TEMPLATE_DIR)" "${COMP_WORDS[1]}"))
    }
   complete -F _ttouch ttouch
else
   echo "Completions for your shell are not supported I guess"
fi
