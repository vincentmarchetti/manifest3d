if [[ -d iiif-prezi3 ]]; then
    echo "iiif-prezi3 already exists. Check and push to remote before deleting";
else
    git clone git@github.com:vincentmarchetti/iiif-prezi3.git
    cd iiif-prezi3 && \
    git branch kshell-main && \
    git checkout kshell-main && \
    git pull --set-upstream origin kshell-main
fi
    