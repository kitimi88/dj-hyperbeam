from django.shortcuts import render,get_object_or_404, redirect
from apps.polls.models import Poll, Choice, Vote
from django.views.generic import DetailView, ListView
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from apps.polls.forms import ChoiceForm
from django.contrib import messages
from django.contrib.auth.models import User

class AllPollsView(ListView):
    model = Poll
    template_name = 'polls/poll_list.html'
    context_object_name = 'polls'
    # paginate_by = 4

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        polls = Poll.objects.all()
        context['poll-list'] = polls
        
        return context


def poll_detail(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    vote_form = ChoiceForm()
    if not poll.active:
        return render(request, 'polls/poll_result.html', {'poll': poll})
    loop_count = poll.choice_set.count()
    context = {
        'poll': poll,
        'vote_form':vote_form,
        'loop_time': range(0, loop_count),
    }
    return render(request, 'polls/poll_detail.html', context)



def poll_vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id) 


    if request.method == 'POST':
        choice_id = request.POST.get('choice')
        vote_form = ChoiceForm(data=request.POST)
        choice = Choice.objects.get(id=choice_id)
        
        if vote_form.is_valid():
            vote = Vote( poll=poll, choice=choice)
           # vote = vote_form.save(commit=False)
            vote.poll = poll
            vote.save()
            print(vote)
            messages.success(request, 'Poll sucessfully recorded. Thanks for voting!',extra_tags='alert alert-success alert-dismissible fade show')
            return render(request, 'polls/poll_result.html', {'poll': poll})
    else:
        vote_form = ChoiceForm()
        messages.error(request, 'Oops. Please select choices.', extra_tags='alert alert-warning alert-dismissible fade show')
        return redirect('polls:detail', poll_id)

    context = {
        'poll':poll,
        'vote_form': vote_form
    }
    
    return render(request, 'polls/poll_result.html',context=context)
